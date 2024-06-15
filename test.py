# import random, winsound


# def loosing_streak_finder(n):
#     CHOICE_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     CHOICE_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] * 10

#     winning_streak = 0
#     max_winning_streak = 0
#     loosing_streak = 0
#     max_loosing_streak = 0

#     for i in range(n):
#         random_1 = random.choice(CHOICE_1)
#         random_2 = random.choice(CHOICE_2)

#         if random_1 == random_2:
#             winning_streak = 0
#             loosing_streak += 1
#             if loosing_streak > max_loosing_streak:
#                 max_loosing_streak = loosing_streak
#         else:
#             loosing_streak = 0
#             winning_streak += 1
#             if winning_streak > max_winning_streak:
#                 max_winning_streak = winning_streak

#     # print(max_winning_streak)
#     # print(max_loosing_streak)
#     # print("done")
#     return loosing_streak


# runs = 0
# loosing_streak = 0
# acceptable_loosing_streak = 4
# n = 2000
# while loosing_streak < acceptable_loosing_streak:
#     loosing_streak = loosing_streak_finder(n)
#     runs += 1

# print(runs)
# print(loosing_streak)
# winsound.Beep(frequency=440, duration=1000)


# stake = 0.35
# total = stake

# for i in range(3):
#     stake *= 11
#     total += stake

# print(total)
# print(total/0.35)

# total = 0
# for balance in range(500, 15000):
#     stake = round(balance / 1490, 2)
#     total = stake
#     for i in range(3):
#         stake = round(stake * 11, 2)
#         total += stake
#     print(balance)
#     print(total)
#     if total > balance:
#         print("oombi")
#         break


# print(0.35 * 1490)