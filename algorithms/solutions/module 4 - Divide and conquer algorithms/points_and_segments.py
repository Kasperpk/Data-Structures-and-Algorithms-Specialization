def points_and_segments_fast(points, segments):
    """
    Efficiently count how many segments contain each point using coordinate compression
    and sweep line algorithm.
    
    Args:
        points: List of points (integers)
        segments: List of segments, each segment is (start, end) tuple
        
    Returns:
        List where result[i] is the number of segments containing points[i]
        
    Time complexity: O((n + m) log (n + m)) where n = number of segments, m = number of points
    Space complexity: O(n + m)
    """
    # Create events for sweep line algorithm
    events = []
    
    # Add segment start and end events
    for start, end in segments:
        events.append((start, 0))  # 0 for segment start
        events.append((end + 1, 1))  # 1 for segment end (end+1 because segments are inclusive)
    
    # Add point events with their original indices
    for i, point in enumerate(points):
        events.append((point, 2, i))  # 2 for point, with original index
    
    # Sort events by coordinate, with tie-breaking: segment starts < points < segment ends
    events.sort(key=lambda x: (x[0], x[1]))
    
    # Process events with sweep line
    active_segments = 0
    result = [0] * len(points)
    
    for event in events:
        if event[1] == 0:  # Segment start
            active_segments += 1
        elif event[1] == 1:  # Segment end
            active_segments -= 1
        else:  # Point
            point_index = event[2]
            result[point_index] = active_segments
    
    return result


# Input/Output handling for Coursera format
if __name__ == "__main__":
    # Read input: first line has number of segments and points
    s, p = map(int, input().split())
    
    segments = []
    for _ in range(s):
        start, end = map(int, input().split())
        segments.append((start, end))
    
    if p == 0:
        points = []
    else:
        points = list(map(int, input().split()))
    
    # Use the efficient algorithm
    result = points_and_segments_fast(points, segments)
    print(' '.join(map(str, result)))
