# ArrayList Implementation and Search Analysis

## Overview

This Python code implements an ArrayList class, allowing the creation of a list with random integer values. The ArrayList class supports sorting and linear/binary search operations. The performance of these search operations is analyzed theoretically and experimentally for varying input sizes.

## Contents

1. [ArrayList Class](#arraylist-class)
2. [Search Methods](#search-methods)
3. [Search Analysis](#search-analysis)
4. [Usage](#usage)

## ArrayList Class

The `ArrayList` class encapsulates a list with random integer values generated during initialization. It includes methods for swapping values, sorting the array, and performing linear and binary searches.

### Methods

- `__init__(self, size)`: Initializes the ArrayList with a list of random integers.
- `swap_values(self, a, b)`: Swaps values at positions a and b in the list.
- `sort_array(self)`: Implements a simple bubble sort to sort the array.
- `linear_search(self, target)`: Performs linear search for the target value.
- `binary_search(self, target)`: Performs binary search on a sorted array.
- `repeat_search_function(self, search_method, target_value, iterations)`: Repeats a search operation multiple times and calculates average time.

## Search Methods

- **Linear Search**: The `linear_search` method iterates through the list linearly to find the target value.
- **Binary Search**: The `binary_search` method uses binary search on a sorted array to find the target value.

## Search Analysis

The search operations are analyzed both theoretically and experimentally. Theoretical complexities are discussed, and experimental results include average search times over multiple iterations.

## Usage

1. Install Python on your machine.
2. Run the script using the command: `python filename.py` (replace `filename.py` with the actual script filename).

Example usage:
```bash
python array_search_analysis.py
