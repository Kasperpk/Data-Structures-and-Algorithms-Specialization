def organize_lottery(points, segments):
    """
    For each point, count how many segments contain it.
    Uses coordinate compression and sorting for efficiency.
    Time complexity: O((n + m) log (n + m))
    """
    # Create events: (coordinate, type, index)
    # type: 0 = left endpoint, 1 = point, 2 = right endpoint
    events = []
    
    # Add segment endpoints
    for i, (start, end) in enumerate(segments):
        events.append((start, 0, i))  # segment start
        events.append((end, 2, i))    # segment end
    
    # Add points
    for i, point in enumerate(points):
        events.append((point, 1, i))  # query point
    
    # Sort events by coordinate, then by type (left endpoint < point < right endpoint)
    events.sort()
    
    # Process events
    active_segments = 0
    result = [0] * len(points)
    
    for coord, event_type, index in events:
        if event_type == 0:  # segment start
            active_segments += 1
        elif event_type == 1:  # query point
            result[index] = active_segments
        else:  # event_type == 2, segment end
            active_segments -= 1
    
    return result

# Alternative implementation using binary search for very large inputs
def organize_lottery_binary_search(points, segments):
    """
    Alternative implementation using binary search.
    May be more efficient for some input distributions.
    """
    result = []
    
    # For each point, count segments that contain it
    for point in points:
        count = 0
        for start, end in segments:
            if start <= point <= end:
                count += 1
        result.append(count)
    
    return result

# Input/Output handling for Coursera format
if __name__ == "__main__":
    # Read segments and points
    s, p = map(int, input().split())
    
    segments = []
    for _ in range(s):
        start, end = map(int, input().split())
        segments.append((start, end))
    
    points = list(map(int, input().split()))
    
    # Solve the problem
    result = organize_lottery(points, segments)
    
    # Output the result
    print(' '.join(map(str, result)))