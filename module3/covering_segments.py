def covering_segments(segments):
    """
    Find the minimum number of points needed to cover all given segments.
    
    Uses greedy algorithm: sort segments by right endpoint, 
    place point at rightmost position of leftmost uncovered segment.
    """
    if not segments:
        return []
    
    # Sort segments by their right endpoint
    segments.sort(key=lambda x: x[1])
    
    points = []
    i = 0
    n = len(segments)
    
    while i < n:
        # Place point at the right end of current segment
        point = segments[i][1]
        points.append(point)
        
        # Skip all segments that are covered by this point
        while i < n and segments[i][0] <= point:
            i += 1
    
    return points

# Input/Output handling for Coursera format
if __name__ == "__main__":
    n = int(input())
    segments = []
    
    for _ in range(n):
        left, right = map(int, input().split())
        segments.append((left, right))
    
    points = covering_segments(segments)
    print(len(points))
    
    if points:
        print(' '.join(map(str, points)))