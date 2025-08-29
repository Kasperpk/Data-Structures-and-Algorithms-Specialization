def max_value_of_loot(capacity, weights, values):
    """
    Maximize the value of loot that can be put into a knapsack of given capacity.
    Items can be broken into fractions (fractional knapsack problem).
    
    Uses greedy algorithm: sort by value-to-weight ratio in descending order.
    """
    n = len(weights)
    # Create list of (value_per_weight, weight, value) tuples
    items = []
    for i in range(n):
        if weights[i] > 0:  # Avoid division by zero
            value_per_weight = values[i] / weights[i]
            items.append((value_per_weight, weights[i], values[i]))
    
    # Sort by value per weight in descending order
    items.sort(reverse=True)
    
    total_value = 0.0
    remaining_capacity = capacity
    
    for value_per_weight, weight, value in items:
        if remaining_capacity == 0:
            break
        
        if weight <= remaining_capacity:
            # Take the whole item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take fraction of the item
            fraction = remaining_capacity / weight
            total_value += value * fraction
            remaining_capacity = 0
    
    return total_value

# Input/Output handling for Coursera format
if __name__ == "__main__":
    n, capacity = map(int, input().split())
    values = []
    weights = []
    
    for _ in range(n):
        v, w = map(int, input().split())
        values.append(v)
        weights.append(w)
    
    result = max_value_of_loot(capacity, weights, values)
    print(f"{result:.10f}")