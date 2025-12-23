import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

PROBABILITY_A = 0.1
PROBABILITY_B = 0.12
SIZE = 600


def simulate_data(size):
    group_a = np.random.binomial(1, PROBABILITY_A, size)  # Конверсия 10%
    group_b = np.random.binomial(1, PROBABILITY_B, size)  # Конверсия 12%
    return group_a, group_b


def mean_and_interval(data):
    mean_a = np.mean(data[0])
    mean_b = np.mean(data[1])
    ci_a = stats.t.interval(
        0.95, len(data[0]) - 1, loc=mean_a, scale=stats.sem(data[0])
    )
    ci_b = stats.t.interval(
        0.95, len(data[1]) - 1, loc=mean_b, scale=stats.sem(data[1])
    )

    return ((mean_a, ci_a), (mean_b, ci_b))


def ab_test(data):
    return stats.ttest_ind(data[0], data[1])


def cohen(data, means):
    return (means[1] - means[0]) / np.sqrt(
        (np.var(data[0], ddof=1) + np.var(data[1], ddof=1)) / 2
    )


def visualization(data):
    plt.figure(figsize=(8, 5))

    plt.hist(data[0], bins=2, alpha=0.6, label="Версия A")
    plt.hist(data[1], bins=2, alpha=0.6, label="Версия B")

    plt.xticks([0, 1])
    plt.xlabel("Конверсия (0 = нет, 1 = да)")
    plt.ylabel("Количество пользователей")
    plt.title("Распределение конверсий: A/B тест")
    plt.legend()

    plt.show()


def main():
    np.random.seed(42)

    data = simulate_data(SIZE)

    group_a_results, group_b_results = mean_and_interval(data)
    print(
        f"Средняя конверсия A: {group_a_results[0]:.4f}, C1: {group_a_results[1]}"
    )
    print(
        f"Средняя конверсия B: {group_b_results[0]:.4f}, CI: {group_b_results[1]}"
    )

    t_stat, p_value = ab_test(data)
    print(f"T-статистика: {t_stat:.4f}, p-value: {p_value:.4f}")
    if p_value < 0.05:
        print("Разница значима: Версия В лучше.")
    else:
        print("Разница не значима.")

    cohen_d = cohen(data, (group_a_results[0], group_b_results[0]))
    print(f"Cohen's d: {cohen_d:.4f}")

    visualization(data)


if __name__ == "__main__":
    main()
