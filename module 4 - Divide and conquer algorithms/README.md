# Module 4 - Divide and Conquer Algorithms

This module contains Python implementations of classic divide and conquer algorithms from the Data Structures and Algorithms Specialization course on Coursera.

## Algorithms Implemented

### 1. Binary Search (`binary_search.py`)
- **Algorithm**: Binary search for finding elements in sorted arrays
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)
- **Features**: Handles duplicates, returns first occurrence
- **Input Format**: Array size, array elements, number of queries, query elements

### 2. Majority Element (`majority_element.py`)
- **Algorithm**: Boyer-Moore Voting Algorithm (optimized) and Divide & Conquer approach
- **Time Complexity**: O(n) for optimized version, O(n log n) for divide & conquer
- **Space Complexity**: O(1) for optimized, O(log n) for divide & conquer
- **Output**: 1 if majority element exists, 0 otherwise
- **Input Format**: Array size, array elements

### 3. Randomized Quick Sort (`sorting.py`)
- **Algorithm**: 3-way quicksort with randomized pivot selection
- **Time Complexity**: O(n log n) average, O(n²) worst case
- **Space Complexity**: O(log n) due to recursion
- **Features**: Efficient handling of duplicates, randomized pivot to avoid worst-case
- **Input Format**: Array size, array elements

### 4. Merge Sort (`merge_sort.py`)
- **Algorithm**: Classic merge sort using divide and conquer
- **Time Complexity**: O(n log n) guaranteed
- **Space Complexity**: O(n)
- **Features**: Stable sorting, consistent performance
- **Input Format**: Array size, array elements

### 5. Counting Inversions (`inversions.py`)
- **Algorithm**: Modified merge sort to count inversions
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)
- **Definition**: Inversion is a pair (i,j) where i < j but arr[i] > arr[j]
- **Input Format**: Array size, array elements

### 6. Points and Segments (`points_and_segments.py`)
- **Algorithm**: Sweep line algorithm with coordinate compression
- **Time Complexity**: O((n+m) log(n+m)) where n=segments, m=points
- **Space Complexity**: O(n+m)
- **Problem**: Count how many segments contain each point
- **Input Format**: Number of segments and points, segment coordinates, point coordinates

### 7. Closest Pair of Points (`closest.py`)
- **Algorithm**: Divide and conquer approach for closest pair problem
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)
- **Problem**: Find minimum distance between any two points in 2D plane
- **Input Format**: Number of points, point coordinates (x, y)

## Usage

Each algorithm file can be run independently with the standard Coursera input format:

```bash
python binary_search.py < input.txt
python majority_element.py < input.txt
python sorting.py < input.txt
# ... etc
```

## Testing

All algorithms have been stress-tested with:
- Large inputs (up to 10,000 elements)
- Edge cases (empty arrays, single elements)
- Worst-case scenarios (reverse-sorted arrays)
- Performance requirements for Coursera grader

## Complexity Guarantees

All implementations are optimized to pass the time and space complexity requirements of the Coursera autograder:
- Binary Search: Passes for arrays up to 10⁵ elements
- Majority Element: Passes for arrays up to 10⁵ elements  
- Sorting: Passes for arrays up to 10⁵ elements
- Inversions: Passes for arrays up to 10⁵ elements
- Points/Segments: Passes for up to 5×10⁴ segments and points
- Closest Points: Passes for up to 10⁵ points