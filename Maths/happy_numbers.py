class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Determine if a number is a happy number.
        
        A happy number is a number defined by the following process:
        - Starting with any positive integer, replace the number by the sum of 
          the squares of its digits.
        - Repeat the process until the number equals 1 (where it will stay), 
          or it loops endlessly in a cycle which does not include 1.
        - Those numbers for which this process ends in 1 are happy numbers.
        
        Approach:
        1. Base cases: If n is 1 or 7, it's a happy number
        2. If n is less than 10 and not 1 or 7, it's not a happy number
        3. Otherwise, calculate the sum of squares of digits and recurse
        
        Mathematical insight: The only single-digit happy numbers are 1 and 7.
        All other single-digit numbers will eventually enter a cycle that 
        doesn't include 1.
        
        Time Complexity: O(log n) - Each step reduces the number of digits
        Space Complexity: O(log n) - Due to recursion stack depth
        
        Args:
            n (int): A positive integer to check
            
        Returns:
            bool: True if n is a happy number, False otherwise
            
        Example:
            >>> solution = Solution()
            >>> solution.isHappy(19)
            True
            >>> solution.isHappy(2)
            False
            >>> solution.isHappy(7)
            True
        """
        if n == 1 or n == 7:
            return True
        elif n < 10:
            return False
        else:
            sum_squares = 0
            while n > 0:
                temp = n % 10
                sum_squares += temp * temp
                n = n // 10
            return self.isHappy(sum_squares)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Happy number
    test1 = 19
    result1 = solution.isHappy(test1)
    print(f"Input: {test1}")
    print(f"Output: {result1}")
    print("Expected: True")
    print(f"Test passed: {result1 is True}\n")
    
    # Test case 2: Not a happy number
    test2 = 2
    result2 = solution.isHappy(test2)
    print(f"Input: {test2}")
    print(f"Output: {result2}")
    print("Expected: False")
    print(f"Test passed: {result2 is False}\n")
    
    # Test case 3: Single digit happy number
    test3 = 7
    result3 = solution.isHappy(test3)
    print(f"Input: {test3}")
    print(f"Output: {result3}")
    print("Expected: True")
    print(f"Test passed: {result3 is True}\n")
    
    # Test case 4: Another happy number
    test4 = 82
    result4 = solution.isHappy(test4)
    print(f"Input: {test4}")
    print(f"Output: {result4}")
    print("Expected: True")
    print(f"Test passed: {result4 is True}\n")
    
    # Test case 5: Single digit non-happy number
    test5 = 4
    result5 = solution.isHappy(test5)
    print(f"Input: {test5}")
    print(f"Output: {result5}")
    print("Expected: False")
    print(f"Test passed: {result5 is False}")
