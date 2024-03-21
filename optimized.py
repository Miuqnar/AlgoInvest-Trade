import time
from pathlib import Path


def read_actions_from_csv(filename):
    """
    Lit un fichier CSV contenant des données sur les actions.

    Args:
        filename (str): Le chemin du fichier CSV.

    Returns:
        list: Une liste d'actions sous forme de tuples (nom, prix, bénéfice).
    """
    with open(filename) as f:
        next(f)  # Ignorer la première ligne (en-tête)
        actions = []
        for line in f:
            name, price_str, benefit_rate_str = line.strip().split(",")
            # convetion le prix de l'action
            # (en centimes)
            price = int(float(price_str) * 100)
            benefit_rate = float(benefit_rate_str)
            # Ignorer les données invalides (prix ou taux de bénéfice négatifs ou égaux à zéro)
            if price <= 0:
                continue
            # Calcule du bénéfice de l'action en multipliant le prix par le taux de bénéfice
            # et en divisant par 100 (pourcentage)
            benefit = int(price * benefit_rate / 100)
            if benefit <= 0:
                continue
            actions.append((name, price, benefit))
    return actions


def knapsack(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    included = [[False] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            name, weight, value = items[i - 1]
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
                if dp[i][w] == dp[i - 1][w - weight] + value:
                    included[i][w] = True
            else:
                dp[i][w] = dp[i - 1][w]

    max_value = dp[n][capacity]
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if included[i][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1][1]

    return max_value, selected_items


if __name__ == "__main__":
    FILENAMES = ['dataset1_Python+P7.csv', 'dataset2_Python+P7.csv']
    # contenir (500 euros convertis en centimes)
    MAX_PRICE = 500 * 100

    for filename in FILENAMES:
        print(f"\nTraitement du fichier '{filename}' en cours...")

        start_time = time.time()
        file_path = str(Path(__file__).parent / filename)
        actions = read_actions_from_csv(file_path)
        best_profit, best_combination = knapsack(actions, MAX_PRICE)

        # Convertion le profit en euros
        best_profit_in_euros = best_profit / 100
        total_price_in_euros = sum(i[1] for i in best_combination) / 100

        print("Meilleur profit possible (en euros) :", best_profit_in_euros)
        print("Prix total des actions (en euros) :", total_price_in_euros)
        end_time = time.time()

        print("Actions sélectionnées (nom, prix, bénéfice) :", best_combination)
        print("Temps écoulé:", round(end_time - start_time, 2), "secondes")


