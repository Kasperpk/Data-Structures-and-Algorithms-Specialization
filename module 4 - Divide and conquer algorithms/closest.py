import math


def distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def closest_pair_brute_force(points):
    """
    Brute force approach for small arrays.
    
    Time complexity: O(n^2)
    """
    n = len(points)
    if n < 2:
        return float('inf')
    
    min_dist = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            min_dist = min(min_dist, distance(points[i], points[j]))
    
    return min_dist


def closest_pair_strip(strip, d):
    """
    Find closest pair in strip of width 2*d.
    
    Args:
        strip: Points in strip sorted by y-coordinate
        d: Current minimum distance
        
    Returns:
        Minimum distance in strip
    """
    min_dist = d
    
    # Check only points that are within distance d
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < min_dist:
            min_dist = min(min_dist, distance(strip[i], strip[j]))
            j += 1
    
    return min_dist


def closest_pair_rec(px, py):
    """
    Recursive divide and conquer function.
    
    Args:
        px: Points sorted by x-coordinate
        py: Points sorted by y-coordinate
        
    Returns:
        Minimum distance between any two points
    """
    n = len(px)
    
    # Base case: use brute force for small arrays
    if n <= 3:
        return closest_pair_brute_force(px)
    
    # Divide
    mid = n // 2
    midpoint = px[mid]
    
    # Split points by y-coordinate
    pyl = [point for point in py if point[0] < midpoint[0] or 
           (point[0] == midpoint[0] and point[1] < midpoint[1])]
    pyr = [point for point in py if point[0] > midpoint[0] or 
           (point[0] == midpoint[0] and point[1] >= midpoint[1])]
    
    # Ensure we don't have empty partitions
    if len(pyl) == 0:
        pyl = [py[0]]
        pyr = py[1:]
    elif len(pyr) == 0:
        pyr = [py[-1]]
        pyl = py[:-1]
    
    # Conquer
    dl = closest_pair_rec(px[:mid], pyl)
    dr = closest_pair_rec(px[mid:], pyr)
    
    # Find minimum of the two halves
    d = min(dl, dr)
    
    # Create strip of points close to the line dividing the two halves
    strip = []
    for point in py:
        if abs(point[0] - midpoint[0]) < d:
            strip.append(point)
    
    # Find closest points in strip
    return min(d, closest_pair_strip(strip, d))


def closest_points(points):
    """
    Find the minimum distance between any two points using divide and conquer.
    
    Args:
        points: List of (x, y) tuples representing points
        
    Returns:
        Minimum distance between any two points
        
    Time complexity: O(n log n)
    Space complexity: O(n)
    """
    if len(points) < 2:
        return 0
    
    # Sort points by x and y coordinates
    px = sorted(points, key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])
    
    return closest_pair_rec(px, py)


# Input/Output handling for Coursera format
if __name__ == "__main__":
    n = int(input())
    points = []
    
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    
    result = closest_points(points)
    print(f"{result:.9f}")