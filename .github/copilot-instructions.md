# AI Agent Instructions for Data Structures and Algorithms Specialization

## Project Overview
This repository contains educational Python implementations of classic algorithms and data structures from the Coursera specialization. The code prioritizes clarity and learning over production optimization.

## Repository Structure
- `/algorithms/solutions/` - Pure Python implementations organized by module (1-5)
- `/algorithms/notebooks/` - Interactive Jupyter notebooks for learning
- `/data-structures/` - Similar structure for data structure implementations

## Code Patterns & Conventions

### Algorithm Implementation Pattern
1. Each algorithm has a primary function with comprehensive docstrings:
```python
def algorithm_name(param1, param2, ...):
    """
    Description of what the algorithm does.
    
    Args:
        param1: Description
        param2: Description
    
    Returns:
        Description of return value
        
    Time complexity: O(...)
    Space complexity: O(...)
    """
```

2. Multiple variants are implemented as separate functions with descriptive suffixes:
   - Base version: `function_name()`
   - Optimized version: `function_name_optimized()`
   - Extended functionality: `function_name_with_x()`

### Input/Output Convention
All solution files follow the Coursera course format:
```python
if __name__ == "__main__":
    # Read input in specified format
    n = int(input())
    values = list(map(int, input().split()))
    
    # Call algorithm
    result = algorithm_name(values)
    
    # Print output in required format
    print(result)
```

### Jupyter Notebook Organization
Notebooks (`*.ipynb`) contain:
1. Problem statement/theory explanation in markdown
2. Implementation with detailed comments
3. Example usage and test cases
4. Visualization of algorithm behavior where applicable

## Common Development Tasks

### Running Solutions
1. Navigate to solution directory:
```bash
cd algorithms/solutions/"module name"
```
2. Run with input from file:
```bash
python3 algorithm_name.py < input.txt
```

### Working with Notebooks
1. Key notebooks for algorithm visualization:
   - `/algorithms/notebooks/DivdeAndConquer.ipynb`
   - `/algorithms/notebooks/DynamicProgramming.ipynb`

2. Data structure concept demonstrations:
   - `/data-structures/notebooks/makeHeap.ipynb`
   - `/data-structures/notebooks/compute_tree_height.ipynb`

## Key Reference Examples

1. Dynamic Programming Pattern:
   - Base example: `algorithms/solutions/module 5 - Dynamic programming/knapsack.py`
   - Shows multiple implementation variants and optimization techniques

2. Graph Algorithm Pattern:
   - Example: `algorithms on graphs/notebooks/CheckConsistency.ipynb`
   - Demonstrates graph representation and traversal techniques

3. Data Structure Implementation:
   - Example: `data-structures/module 2/problems/MakeHeap.py`
   - Shows class-based data structure implementation with operation methods