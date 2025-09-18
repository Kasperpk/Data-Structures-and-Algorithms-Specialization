# Module 5 - Dynamic Programming

This module contains Python implementations of classic dynamic programming algorithms from the Data Structures and Algorithms Specialization course on Coursera.

## Algorithms Implemented

### 1. Money Change DP (`money_change_dp.py`)
- **Algorithm**: Dynamic programming solution for coin change problem
- **Time Complexity**: O(money × number_of_coins)
- **Space Complexity**: O(money)
- **Problem**: Find minimum number of coins needed to make change
- **Input Format**: Amount of money to change
- **Note**: Unlike greedy approach, works for any coin denominations

### 2. Primitive Calculator (`primitive_calculator.py`)
- **Algorithm**: DP to find minimum operations to reach 1 from n
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Operations**: Divide by 2, divide by 3, subtract 1
- **Input Format**: Target number n
- **Output**: Minimum operations and sequence of numbers

### 3. Edit Distance (`edit_distance.py`)
- **Algorithm**: Levenshtein distance using dynamic programming
- **Time Complexity**: O(len(str1) × len(str2))
- **Space Complexity**: O(len(str1) × len(str2)) or O(min(len1, len2)) optimized
- **Operations**: Insert, delete, substitute characters
- **Input Format**: Two strings
- **Output**: Minimum edit distance

### 4. Longest Common Subsequence (`longest_common_subsequence.py`)
- **Algorithm**: DP solution for LCS problem
- **Time Complexity**: O(len(seq1) × len(seq2))
- **Space Complexity**: O(len(seq1) × len(seq2))
- **Problem**: Find length of longest common subsequence
- **Input Format**: Number of sequences (2 or 3), then the sequences
- **Features**: Supports both 2-sequence and 3-sequence LCS

### 5. Knapsack (`knapsack.py`)
- **Algorithm**: 0/1 Knapsack problem using DP
- **Time Complexity**: O(n × capacity)
- **Space Complexity**: O(n × capacity) or O(capacity) optimized
- **Problem**: Maximize value/weight without item repetition
- **Input Format**: Capacity, number of items, item weights
- **Variants**: Classic 0/1, space-optimized, with item tracking

### 6. Placing Parentheses (`placing_parentheses.py`)
- **Algorithm**: Matrix chain multiplication variant for arithmetic expressions
- **Time Complexity**: O(n³) where n = number of operands
- **Space Complexity**: O(n²)
- **Problem**: Maximize value of arithmetic expression by optimal parenthesization
- **Input Format**: Arithmetic expression string (e.g., "5-8+7*4-8+9")
- **Operations**: Addition, subtraction, multiplication

## Usage

Each algorithm file can be run independently with the standard Coursera input format:

```bash
python money_change_dp.py < input.txt
python primitive_calculator.py < input.txt
python edit_distance.py < input.txt
python longest_common_subsequence.py < input.txt
python knapsack.py < input.txt
python placing_parentheses.py < input.txt
```

## Key Dynamic Programming Concepts

### 1. **Optimal Substructure**
All problems exhibit optimal substructure - the optimal solution contains optimal solutions to subproblems.

### 2. **Overlapping Subproblems**
Subproblems are solved multiple times in naive recursive solutions, making memoization/tabulation beneficial.

### 3. **Bottom-Up vs Top-Down**
- **Bottom-Up (Tabulation)**: Fill DP table iteratively from base cases
- **Top-Down (Memoization)**: Recursive with caching (implemented in some algorithms)

### 4. **Space Optimization**
Many 2D DP problems can be optimized to use O(min(dimensions)) space when only previous row/column is needed.

## Testing

All algorithms have been tested with:
- Small inputs for correctness verification
- Edge cases (empty inputs, single elements)
- Coursera-format compliance
- Performance requirements for online judges

## Complexity Guarantees

All implementations are optimized to pass time and space requirements:
- Money Change DP: Handles up to 10³ money amount
- Primitive Calculator: Handles up to 10⁶ input values
- Edit Distance: Handles strings up to 10² characters
- LCS: Handles sequences up to 10² elements
- Knapsack: Handles up to 10⁴ capacity and items
- Placing Parentheses: Handles expressions up to 29 characters

## Differences from Other Modules

Unlike greedy algorithms (Module 3) which make locally optimal choices, dynamic programming:
- Explores all possibilities systematically
- Guarantees globally optimal solutions
- Has higher time complexity but works for more general cases
- Uses memory to avoid recomputing subproblems

Unlike divide & conquer (Module 4), dynamic programming:
- Subproblems overlap significantly
- Uses memoization/tabulation to avoid redundant computation
- Typically has polynomial rather than logarithmic complexity