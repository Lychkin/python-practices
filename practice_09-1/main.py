import os
import csv
from datetime import datetime
import requests
from dotenv import load_dotenv
from tabulate import tabulate
import argparse


def validate_date(date_str: str) -> str:
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"Неверный формат даты: {date_str}. Используйте YYYY-MM-DD."
        )


def handle_api_errors(response):
    if response.status_code == 401:
        raise RuntimeError("Ошибка 401: Неверный OAuth-токен.")

    if response.status_code == 403:
        raise RuntimeError(
            "Ошибка 403: Неверный OAuth-токен или нет доступа к счётчику."
        )

    if response.status_code == 404:
        raise RuntimeError("Ошибка 404: Указанный счётчик не найден.")

    if response.status_code == 400:
        try:
            detail = response.json().get("message", "Некорректный запрос.")
        except:
            detail = "Некорректный запрос."
        raise RuntimeError(f"Ошибка 400: {detail}")

    if not response.ok:
        raise RuntimeError(
            f"Неизвестная ошибка API ({response.status_code}): {response.text}"
        )


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--date1", required=True, type=validate_date)

    parser.add_argument("--date2", required=True, type=validate_date)

    args = parser.parse_args()

    date1 = args.date1
    date2 = args.date2

    if datetime.strptime(date1, "%Y-%m-%d") > datetime.strptime(
        date2, "%Y-%m-%d"
    ):
        raise ValueError("Ошибка: дата начала периода позже даты окончания.")

    load_dotenv()

    TOKEN = os.getenv("YANDEX_TOKEN")
    COUNTER_ID = os.getenv("COUNTER_ID")

    if not TOKEN or not COUNTER_ID:
        raise RuntimeError(
            "Ошибка: отсутствуют YANDEX_TOKEN или COUNTER_ID в .env файле."
        )

    API_URL = "https://api-metrika.yandex.net/stat/v1/data"

    params = {
        "ids": COUNTER_ID,
        "metrics": "ym:s:visits,ym:s:pageviews,ym:s:users",
        "date1": date1,
        "date2": date2,
    }

    headers = {"Authorization": f"OAuth {TOKEN}"}

    response = requests.get(API_URL, params=params, headers=headers)

    try:
        handle_api_errors(response)
    except RuntimeError as error:
        print(error)
        return

    try:
        data = response.json()
        visits, pageviews, users = data["totals"]
    except Exception:
        print("Ошибка обработки ответа API. Проверьте параметры.")
        return

    table_data = [
        ["Визиты", visits],
        ["Просмотры", pageviews],
        ["Уникальные пользователи", users],
    ]

    print(
        tabulate(
            table_data, headers=["Показатель", "Значение"], tablefmt="github"
        )
    )

    os.makedirs("data", exist_ok=True)
    CSV_FILE_NAME = "metrika_report.csv"
    with open(
        f"data/{CSV_FILE_NAME}", "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file)
        writer.writerow(["metric", "value"])
        writer.writerow(["visits", visits])
        writer.writerow(["pageviews", pageviews])
        writer.writerow(["users", users])


if __name__ == "__main__":
    main()
