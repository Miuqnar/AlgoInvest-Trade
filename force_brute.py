import itertools
import time

budget_max = 500

ACTIONS = [

    ("Action-1", 20, 0.05),
    ("Action-2", 30, 0.10),
    ("Action-3", 50, 0.15),
    ("Action-4", 70, 0.20),
    ("Action-5", 60, 0.17),
    ("Action-6", 80, 0.25),
    ("Action-7", 22, 0.07),
    ("Action-8", 26, 0.11),
    ("Action-9", 48, 0.13),
    ("Action-10", 34, 0.27),
    ("Action-11", 42, 0.17),
    ("Action-12", 110, 0.09),
    ("Action-13", 38, 0.23),
    ("Action-14", 14, 0.01),
    ("Action-15", 18, 0.03),
    ("Action-16", 8, 0.08),
    ("Action-17", 4, 0.12),
    ("Action-18", 10, 0.14),
    ("Action-19", 24, 0.21),
    ("Action-20", 114, 0.18)

]


def calculate_profit(combination):
    """
    Calcule le coût total et le profit total pour une combinaison donnée d'actions.

    Args:
        combination (tuple): Une combinaison d'actions à évaluer.

    Returns:
        tuple: Un tuple contenant le coût total et le profit total de la combinaison.
    """
    cost = sum(action[1] for action in combination)
    profit = sum(action[1] * action[2] for action in combination)

    return cost, profit


def find_best_combination(budget):
    """
    Trouve la meilleure combinaison d'actions qui respecte le budget donné.

    Args:
        budget (int): Le budget maximum disponible pour les actions.

    Returns:
        tuple: Un tuple contenant le meilleur profit atteignable et la combinaison correspondante.
    """
    current_best_profit = 0
    current_best_combination = None
    for combination_size in range(1, len(ACTIONS) + 1):
        for combination in itertools.combinations(ACTIONS, combination_size):
            total_cost, total_profit = calculate_profit(combination)

            if total_cost <= budget and total_profit > current_best_profit:
                current_best_profit = total_profit
                current_best_combination = combination

    return current_best_profit, current_best_combination


start_time = time.time()
best_profit, best_combination = find_best_combination(budget_max)

print("Meilleur bénéfice de tous les combinaisons:", round(best_profit, 2), "euros")
print("Meilleur Combinaison:", best_combination)

end_time = time.time()
elapsed_time = end_time - start_time
print(f" \nTemps écoulé: {elapsed_time:.2f} secondes", end="", flush=True)  # Formatage des chaînes .2f
