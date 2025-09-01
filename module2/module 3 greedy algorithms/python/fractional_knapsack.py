def maximum_loot(w,weights,costs):
    if w == 0 or not weights:
        return 0
    max_item = 0
    m = -1
    for i in range(0,len(weights)):
        if costs[i]/weights[i] > max_item:
           max_item = costs[i]/weights[i]
           m = m + 1
           print(f'found new max value item at index {m}')
    print(f'found highest value item at index {m} which costs {costs[m]} and weights {weights[m]}')

    amount = min(weights[m], w)

    value = costs[m] * (amount/weights[m])
    print(f'adding a total amount to the knapsack of {value}')
    weights.pop(m)
    costs.pop(m)

    return value + maximum_loot(w-amount,weights,costs)

if __name__ == "__main__":
    w = int(input())
    weights = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    result = maximum_loot(w,weights,costs)
    print(result)