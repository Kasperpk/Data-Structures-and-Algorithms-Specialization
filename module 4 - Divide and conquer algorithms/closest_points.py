import math

def distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def brute_force_closest(points):
    """Brute force approach for small arrays."""
    min_dist = float('inf')
    n = len(points)
    
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(points[i], points[j])
            min_dist = min(min_dist, dist)
    
    return min_dist

def closest_in_strip(strip, d):
    """Find closest distance in a strip of points."""
    min_dist = d
    
    # Sort strip by y-coordinate
    strip.sort(key=lambda point: point[1])
    
    # Find the closest points in strip
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < min_dist:
            min_dist = min(min_dist, distance(strip[i], strip[j]))
            j += 1
    
    return min_dist

def closest_pair_rec(px, py):
    """
    Recursive divide and conquer algorithm to find closest pair.
    px: points sorted by x-coordinate
    py: points sorted by y-coordinate
    """
    n = len(px)
    
    # Base case: use brute force for small arrays
    if n <= 3:
        return brute_force_closest(px)
    
    # Divide
    mid = n // 2
    midpoint = px[mid]
    
    pyl = [point for point in py if point[0] <= midpoint[0]]
    pyr = [point for point in py if point[0] > midpoint[0]]
    
    # Conquer
    dl = closest_pair_rec(px[:mid], pyl)
    dr = closest_pair_rec(px[mid:], pyr)
    
    # Find minimum of the two distances
    d = min(dl, dr)
    
    # Create an array of points close to the line dividing the two halves
    strip = [point for point in py if abs(point[0] - midpoint[0]) < d]
    
    # Find the closest points in strip
    return min(d, closest_in_strip(strip, d))

def closest_pair(points):
    """
    Find the minimum distance between any two points.
    Time complexity: O(n log n)
    """
    if len(points) < 2:
        return float('inf')
    
    # Sort points by x and y coordinates
    px = sorted(points, key=lambda point: point[0])
    py = sorted(points, key=lambda point: point[1])
    
    return closest_pair_rec(px, py)

# Input/Output handling for Coursera format
if __name__ == "__main__":
    n = int(input())
    points = []
    
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    
    result = closest_pair(points)
    print(f"{result:.9f}")  # Print with high precision