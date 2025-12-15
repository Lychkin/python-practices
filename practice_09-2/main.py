import os
import json
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
API_VERSION = os.getenv("API_VERSION")


def get_likes(owner_id, post_id):
    url = "https://api.vk.com/method/likes.getList"
    params = {
        "type": "post",
        "owner_id": owner_id,
        "item_id": post_id,
        "count": 1000,
        "extended": 0,
        "access_token": ACCESS_TOKEN,
        "v": API_VERSION,
    }

    users = []
    offset = 0

    while True:
        params["offset"] = offset
        response = requests.get(url, params=params).json()
        items = response["response"]["items"]

        if not items:
            break

        users.extend(items)
        offset += 1000

    return users


def get_users_info(user_ids):
    url = "https://api.vk.com/method/users.get"
    users_info = []
    group_size = 100

    for i in range(0, len(user_ids), group_size):
        group = user_ids[i : i + group_size]
        params = {
            "user_ids": ",".join(map(str, group)),
            "fields": "sex,bdate",
            "access_token": ACCESS_TOKEN,
            "v": API_VERSION,
        }
        response = requests.get(url, params=params).json()
        if "response" in response:
            users_info.extend(response["response"])

    return users_info


def get_age(bdate):
    try:
        birth_date = datetime.strptime(bdate, "%d.%m.%Y")
        today = datetime.today()
        return today.year - birth_date.year
    except Exception:
        return None


def build_statistics(post, users):
    age_stat = {"0-18": 0, "19-35": 0, "36-50": 0, ">50": 0, "unknown": 0}

    sex_stat = {"male": 0, "female": 0, "unknown": 0}

    for user in users:
        if user.get("sex") == 1:
            sex_stat["female"] += 1
        elif user.get("sex") == 2:
            sex_stat["male"] += 1
        else:
            sex_stat["unknown"] += 1

        age = get_age(user.get("bdate", ""))
        if age is None:
            age_stat["unknown"] += 1
        elif age <= 18:
            age_stat["0-18"] += 1
        elif age <= 35:
            age_stat["19-35"] += 1
        elif age <= 50:
            age_stat["36-50"] += 1
        else:
            age_stat[">50"] += 1

    statistics = {"post_id": post, "age": age_stat, "sex": sex_stat}

    return statistics


def main():
    owner_id = int(os.getenv("OWNER_ID"))
    post_id = int(os.getenv("POST_ID"))

    like_ids = get_likes(owner_id, post_id)
    users_info = get_users_info(like_ids)
    result = build_statistics(post_id, users_info)

    return result


if __name__ == "__main__":
    stats = main()
    os.makedirs("data", exist_ok=True)
    with open("data/stats.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=4)
    print(stats)
