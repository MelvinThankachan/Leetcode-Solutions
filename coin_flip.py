import random

CHOICE = ["E", "O"] * 18 + ["Z"]

initial_balance = 20000
balance = initial_balance
initial_stake = 20
stake = 200
target = float("inf")
max_drawdown = 0
max_profit = 0
max_stake = 0
winning_streak = 0
losing_streak = 0
max_winning_streak = 0
max_losing_streak = 0
rounds = 0
max_rounds = 20000

while balance < initial_balance + target:
    rounds += 1
    balance -= stake

    flip = random.choice(CHOICE)

    if flip == "E":
        balance += 2 * stake
        winning_streak += 1
        losing_streak = 0
        if stake <= balance:
            stake -= initial_stake
    else:
        if stake != initial_stake:
            stake += initial_stake
        losing_streak -= 1
        winning_streak = 0

    profit = balance - initial_balance

    if winning_streak > max_winning_streak:
        max_winning_streak = winning_streak
    if losing_streak > max_losing_streak:
        max_losing_streak = losing_streak
    if stake > max_stake:
        max_stake = stake
    if balance < initial_balance and profit < max_drawdown:
        max_drawdown = profit
    if balance > initial_balance and profit > max_profit:
        max_profit = profit

    if balance < 0 or stake > balance or rounds == max_rounds:
        break

print(f"Number of rounds played: {rounds}")
print(
    f"Max Winning streak: {max_winning_streak}, Max Losing Streak: {max_losing_streak}"
)
print(
    f"Max Drawdown: {max_drawdown}, Max Profit: {max_profit}, Max Stake Placed: {max_stake}"
)
print(f"Total Balance: {balance}, Profit: {balance-initial_balance}")
if balance > initial_balance:
    print("Jayichu Mwone")
