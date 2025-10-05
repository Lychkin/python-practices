def count_votes(votes):
    votes_counter = {}
    for vote in votes.split():
        try:
            valid_vote = int(vote)
            if valid_vote > 0:
                if valid_vote in votes_counter:
                    votes_counter[valid_vote] += 1
                else:
                    votes_counter[valid_vote] = 1
        except ValueError:
            pass
    votes_counter = dict(
        sorted(votes_counter.items(), key=lambda item: item[1], reverse=True)
    )
    return votes_counter


def main():
    with open("data/input_for_task3.txt", encoding="utf-8") as file:
        votes_results = file.read()
        party_results = count_votes(votes_results)
        votes_sum = sum(party_results.values())
        for party_index, party_result in enumerate(party_results):
            print(
                f"{party_index+1}. Партия #{party_result} | "
                + f"{party_results[party_result]} | "
                + f"{round(party_results[party_result] / votes_sum * 100, 2)}%"
            )


if __name__ == "__main__":
    main()
