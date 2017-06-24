# import random
# def roll_die():
#     return random.randrange(1, 7)
#
# def play_turn():
#     total = roll_die() + roll_die()
#
#     if total == 12:
#         return 1.5
#     elif total == 11:
#         return 1.0
#     elif total == 10:
#         return 0.5
#     elif total <= 6:
#         return -0.5
#     else:  # total is 7, 8, or 9
#         return 0
#
# from collections import Counter
# counts = Counter(play_turn() for i in range(100000))
# # counts
# probabilities = {score: count / 100000.0 for score, count in counts.items()}
# print(probabilities)
