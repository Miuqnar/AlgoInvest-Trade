# def knapsack(items, capacity):
#     n = len(items)
#     dp = [[0] * (capacity + 1) for _ in range(n + 1)]
#     included = [[False] * (capacity + 1) for _ in range(n + 1)]
#
#     for i in range(1, n + 1):
#         for w in range(1, capacity + 1):
#             name, weight, value = items[i - 1]
#             if weight <= w:
#                 dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
#                 if dp[i][w] == dp[i - 1][w - weight] + value:
#                     included[i][w] = True
#             else:
#                 dp[i][w] = dp[i - 1][w]
#
#     max_value = dp[n][capacity]
#     selected_items = []
#     w = capacity
#     for i in range(n, 0, -1):
#         if included[i][w]:
#             selected_items.append(items[i - 1])
#             w -= items[i - 1][1]
#
#     return max_value, selected_items
#
# # Example usage:
# items = [("Item 1", 2, 10), ("Item 2", 3, 7), ("Item 3", 4, 14), ("Item 4", 5, 8)]
# capacity = 7
# max_value, best_combination = knapsack(items, capacity)
# print("Max value:", max_value)
# print("Best combination:")
# for item in best_combination:
#     print(f"- {item[0]}: weight={item[1]}, value={item[2]}")
#
#
#
# def remove_consonants_and_reversed(text):
#     vowels = "aeiou"
#     text = "".join([c for c in text if c.lower() in vowels])
#     return text[::-1]
#
# text = "aaaaaaaa"
# print(remove_consonants(text))
#
# force brut
# # Time complexity: O(2^n)
# # Space complexity: O(n)
# knap sack
# # Time complexity: O(n*W)
# # Space complexity: O(n*W)
#
# 1. 20 action Force Brute (trop de temps)
# 2. knapsack 20 actions .... (comparer le temps d'execution et resultats)
# 3. knapsack 1000 action et comparer avec Siena
