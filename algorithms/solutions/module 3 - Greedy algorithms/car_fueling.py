def car_fueling(distance, tank_capacity, stops):
    """
    Find the minimum number of refills needed to travel the given distance.
    
    Uses greedy algorithm: refill only when necessary, and when refilling,
    go to the farthest gas station reachable.
    """
    # Add start and end points
    all_stops = [0] + stops + [distance]
    all_stops.sort()
    
    n = len(all_stops)
    refills = 0
    current_position = 0
    
    for i in range(1, n):
        # Check if the gap between consecutive stops is too large
        if all_stops[i] - all_stops[i-1] > tank_capacity:
            return -1  # Impossible to make the trip
    
    i = 0
    while i < n - 1:
        # Find the farthest stop reachable with current fuel
        farthest = i
        while farthest < n - 1 and all_stops[farthest + 1] - all_stops[i] <= tank_capacity:
            farthest += 1
        
        if farthest == i:
            # Can't reach any further stop
            return -1
        
        if farthest == n - 1:
            # Can reach the destination
            break
        
        # Need to refill at position 'farthest'
        refills += 1
        i = farthest
    
    return refills

# Input/Output handling for Coursera format
if __name__ == "__main__":
    distance = int(input())
    tank_capacity = int(input())
    n = int(input())
    
    if n == 0:
        stops = []
    else:
        stops = list(map(int, input().split()))
    
    result = car_fueling(distance, tank_capacity, stops)
    print(result)