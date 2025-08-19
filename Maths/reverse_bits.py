class Solution(object):
    def reverseBits(self, n):
        """
        Reverse bits of a given 32 bits unsigned integer.

        This function takes a 32-bit unsigned integer and returns the integer
        with its bits reversed. For example, if the input is 43261596
        (binary: 00000010100101000001111010011100), the output should be
        964176192 (binary: 00111001011110000010100101000000).

        Approach:
        1. Initialize a result variable to 0
        2. Iterate through all 32 bits of the input number
        3. For each iteration:
           - Shift the result left by 1 bit to make room for the next bit
           - Extract the least significant bit of the input using (n & 1)
           - Add this bit to the result
           - Right shift the input by 1 bit to process the next bit
        4. Return the final result

        Time Complexity: O(1) - We always iterate exactly 32 times
        Space Complexity: O(1) - We use only a constant amount of extra space

        Args:
            n (int): A 32-bit unsigned integer

        Returns:
            int: The integer with its bits reversed

        Example:
            >>> solution = Solution()
            >>> solution.reverseBits(43261596)
            964176192
            >>> solution.reverseBits(4294967293)
            3221225471
        """
        temp = 0
        for i in range(32):
            temp = temp << 1
            temp = temp + (n & 1)
            n = n >> 1
        return temp


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Example from problem
    test1 = 43261596
    result1 = solution.reverseBits(test1)
    print(f"Input: {test1} (binary: {bin(test1)[2:].zfill(32)})")
    print(f"Output: {result1} (binary: {bin(result1)[2:].zfill(32)})")
    print("Expected: 964176192")
    print(f"Test passed: {result1 == 964176192}\n")

    # Test case 2: Another example
    test2 = 4294967293
    result2 = solution.reverseBits(test2)
    print(f"Input: {test2} (binary: {bin(test2)[2:].zfill(32)})")
    print(f"Output: {result2} (binary: {bin(result2)[2:].zfill(32)})")
    print("Expected: 3221225471")
    print(f"Test passed: {result2 == 3221225471}\n")

    # Test case 3: All zeros
    test3 = 0
    result3 = solution.reverseBits(test3)
    print(f"Input: {test3} (binary: {bin(test3)[2:].zfill(32)})")
    print(f"Output: {result3} (binary: {bin(result3)[2:].zfill(32)})")
    print("Expected: 0")
    print(f"Test passed: {result3 == 0}\n")

    # Test case 4: All ones
    test4 = 4294967295
    result4 = solution.reverseBits(test4)
    print(f"Input: {test4} (binary: {bin(test4)[2:].zfill(32)})")
    print(f"Output: {result4} (binary: {bin(result4)[2:].zfill(32)})")
    print("Expected: 4294967295")
    print(f"Test passed: {result4 == 4294967295}")
