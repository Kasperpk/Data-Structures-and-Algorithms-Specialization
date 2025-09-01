def money_change(money):
    numCoins = 0

    while money > 0:
        if money >= 10:
            money = money - 10
        elif money >= 5:
            money = money - 5
        else:
            money = money - 1
        numCoins += 1

    return numCoins

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    n = int(input())
    coins_used = money_change(n)
    print(coins_used)
