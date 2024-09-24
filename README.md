Here's an updated version of the `README.md` to reflect that the solutions may be in various languages, with a focus on Python 3:

---

# LeetCode Solutions Repository

This repository contains solutions to a wide range of LeetCode problems. Each solution is provided as either a function or class definition in various programming languages, including Python (mostly Python 3) and occasionally other languages like C, depending on the problem type.

The goal of this repository is to offer clean, standalone solutions to specific problems, allowing others to easily integrate these solutions into their projects by calling the functions/classes as needed.

## Repository Structure

The repository is organized by problem type, with each folder corresponding to a problem category. For example:

```
.
├── Arrays
├── Strings
├── LinkedLists
├── DynamicProgramming
├── Trees
└── Graphs
```

Each folder contains files named after the problem (usually by problem number or name), with one function or class per file. The solutions are mainly written in Python 3, but some may be in C or other languages.

## Supported Languages

- **Python 3** (majority of solutions)
- **C** (occasionally used for specific problems)
- Other languages may be added in the future based on problem requirements.

## How to Use

To use a solution from this repository:

1. **Find the solution**: Navigate through the directory structure to find the solution file that matches the problem you're working on (e.g., `two_sum.py` or `merge_sorted_lists.c`).
2. **Copy the function/class**: The solution is typically a single function or class. Copy it into your project.
3. **Call the function/class** with appropriate input in your environment. Below are examples for both Python and C usage.

### Example 1: Using a Python Function

Suppose you're solving a problem like "Two Sum" (Problem #1) in Python. You would find the corresponding file in the `Arrays` directory (e.g., `two_sum.py`), copy the function, and use it as follows:

**two_sum.py:**
```python
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        if target - num in num_map:
            return [num_map[target - num], i]
        num_map[num] = i
```

**Usage:**
```python
from two_sum import two_sum

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]
```

### Example 2: Using a C Function

For problems solved in C, you can integrate the code in your project by copying the function from the file (e.g., `merge_sorted_lists.c`), compiling it, and calling it in your program:

**merge_sorted_lists.c:**
```c
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
    // Implementation of the merge logic
}
```

You would compile the file and then link it to your project.

**Usage (in C project):**
```c
#include "merge_sorted_lists.c"

int main() {
    // Code to initialize lists and call mergeTwoLists
}
```

## Contributing

You are welcome to contribute solutions in any programming language (Python, C, etc.). Here’s how to contribute:

1. Fork the repository.
2. Add your solution to the appropriate category folder.
3. Ensure the solution is a standalone function or class without additional code like input/output handling.
4. Submit a pull request.

### Guidelines:
- Write clean, efficient code.
- Ensure that your solution is properly placed in the correct directory (e.g., `Arrays`, `Trees`, etc.).
- Python 3 is the preferred language, but C and other languages are welcome.

## LeetCode Problem Categories

This repository contains solutions across a wide range of categories, including:

- Arrays
- Strings
- Linked Lists
- Dynamic Programming
- Trees
- Graphs
- Math
- Sorting and Searching

Each category will contain solutions relevant to that topic.

## Notes

- The majority of solutions are written in **Python 3**, with occasional solutions in **C** and other languages.
- Each file contains only the function or class definition needed to solve the problem. It does not include any test cases, input/output handling, or main function.
- If you are unfamiliar with a problem, refer to [LeetCode](https://leetcode.com/) for the full problem statement before using the solution.
- The goal is to provide solutions that are optimized for readability and performance.

## License

This repository is open-source under the MIT License. Feel free to use, modify, and distribute the code.

## Contact

If you have any questions or suggestions, feel free to reach out via GitHub issues.

---
