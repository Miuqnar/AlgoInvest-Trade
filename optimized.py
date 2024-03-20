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
            if price <= 0 or benefit_rate <= 0:
                continue
            # Calculer le bénéfice de l'action en multipliant le prix par le taux de bénéfice
            # et en divisant par 100 (pourcentage)
            benefit = int(price * benefit_rate / 100)
            actions.append((name, price, benefit))
    return actions


def knapsack(actions, max_price):
    """
    Résout le problème du sac à dos pour maximiser le bénéfice.

    Args:
        actions (list): Une liste d'actions sous forme de tuples (nom, prix, bénéfice).
        max_price (int): Le prix maximal autorisé dans le sac à dos.

    Returns:
        tuple: Un tuple contenant le bénéfice total et les actions sélectionnées.
    """
    n = len(actions)
    dp = [0] * (max_price + 1)

    for i in range(n):
        for j in range(max_price, actions[i][1] - 1, -1):
            dp[j] = max(dp[j], dp[j - actions[i][1]] + actions[i][2])

    return dp[max_price]


if __name__ == "__main__":
    FILENAMES = ['dataset1_Python+P7.csv', 'dataset2_Python+P7.csv']
    MAX_PRICE = 500

    for filename in FILENAMES:
        print(f"\nTraitement du fichier '{filename}' en cours...")

        start_time = time.time()
        file_path = str(Path(__file__).parent / filename)
        actions = read_actions_from_csv(file_path)
        best_price = knapsack(actions, MAX_PRICE)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Temps écoulé pour '{filename}': {elapsed_time:.2f} secondes")

        print(f"Meilleur bénéfice obtenu pour '{filename}': {int(str(best_price)) / 100:.2f}")

        # Affichage de la meilleure combinaison d'actions sélectionnées
        selected_actions = []
        remaining_price = MAX_PRICE
        for action in actions[::-1]:
            # [::-1]
            # parcourt les éléments de la liste actions en commençant par le
            # dernier élément et en se déplaçant vers le premier élément.
            if action[1] <= remaining_price and knapsack(actions, remaining_price - action[1]) + action[2] == best_price:
                selected_actions.append(action)
                remaining_price -= action[1]
        print("Meilleure combinaison d'actions sélectionnées :")
        for action in selected_actions:
            print(f"Nom: {action[0]}, Prix: {action[1] / 100}, Bénéfice: {action[2]}")
