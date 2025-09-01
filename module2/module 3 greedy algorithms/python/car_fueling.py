def car_fueling(d, m, stops):
    # Add start (0) and destination (d) to stops
    stops = [0] + stops + [d]
    num_refills = 0
    curr_pos = 0

    while curr_pos < len(stops) - 1:
        last_pos = curr_pos
        # Go as far as possible without refilling
        while (curr_pos < len(stops) - 1) and (stops[curr_pos + 1] - stops[last_pos] <= m):
            curr_pos += 1
        # If we haven't moved, can't reach next stop
        if curr_pos == last_pos:
            return -1
        # If not at destination, need to refill
        if curr_pos < len(stops) - 1:
            num_refills += 1

    return num_refills

if __name__ == "__main__":
    d, m, n = map(int, input("Enter d, m, n: ").split())
    stops = list(map(int, input(f"Enter {n} gas station stops: ").split()))
    print(car_fueling(d, m, stops))