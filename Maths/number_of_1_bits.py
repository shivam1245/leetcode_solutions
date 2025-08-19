class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Count the number of '1' bits in a given integer (Hamming weight).

        This function takes a 32-bit unsigned integer and returns the number
        of '1' bits in its binary representation. For example, if the input
        is 11 (binary: 1011), the output should be 3.

        Approach (Brian Kernighan's Algorithm):
        1. Initialize a counter to 0
        2. While n is not zero:
           - Perform n = n & (n-1) to clear the least significant '1' bit
           - Increment the counter
        3. Return the counter

        The key insight is that n & (n-1) always clears the least significant
        '1' bit. This is because:
        - n-1 flips all bits after the least significant '1' bit
        - n & (n-1) clears only the least significant '1' bit
        - Each iteration removes exactly one '1' bit

        Time Complexity: O(k) where k is the number of '1' bits
        Space Complexity: O(1) - We use only a constant amount of extra space

        Args:
            n (int): A 32-bit unsigned integer

        Returns:
            int: The number of '1' bits in the binary representation of n

        Example:
            >>> solution = Solution()
            >>> solution.hammingWeight(11)
            3
            >>> solution.hammingWeight(128)
            1
            >>> solution.hammingWeight(4294967293)
            31
        """
        temp = 0
        while n != 0:
            n = n & (n - 1)
            temp += 1
        return temp


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Example from problem
    test1 = 11
    result1 = solution.hammingWeight(test1)
    print(f"Input: {test1} (binary: {bin(test1)[2:].zfill(32)})")
    print(f"Output: {result1}")
    print("Expected: 3")
    print(f"Test passed: {result1 == 3}\n")

    # Test case 2: Power of 2 (only one '1' bit)
    test2 = 128
    result2 = solution.hammingWeight(test2)
    print(f"Input: {test2} (binary: {bin(test2)[2:].zfill(32)})")
    print(f"Output: {result2}")
    print("Expected: 1")
    print(f"Test passed: {result2 == 1}\n")

    # Test case 3: Zero (no '1' bits)
    test3 = 0
    result3 = solution.hammingWeight(test3)
    print(f"Input: {test3} (binary: {bin(test3)[2:].zfill(32)})")
    print(f"Output: {result3}")
    print("Expected: 0")
    print(f"Test passed: {result3 == 0}\n")

    # Test case 4: All ones except one bit
    test4 = 4294967293
    result4 = solution.hammingWeight(test4)
    print(f"Input: {test4} (binary: {bin(test4)[2:].zfill(32)})")
    print(f"Output: {result4}")
    print("Expected: 31")
    print(f"Test passed: {result4 == 31}\n")

    # Test case 5: Multiple '1' bits
    test5 = 255
    result5 = solution.hammingWeight(test5)
    print(f"Input: {test5} (binary: {bin(test5)[2:].zfill(32)})")
    print(f"Output: {result5}")
    print("Expected: 8")
    print(f"Test passed: {result5 == 8}")
