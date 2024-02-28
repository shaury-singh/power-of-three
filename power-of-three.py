class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        loop = 1
        isPower = 1
        i = 1
        while loop == 1:
            if i<n:
                i = i*3
            if i == n:
                loop = 2
            if i>n:
                isPower = 0
                loop = 2
        if isPower == 1:
            return True
        else:
            return False
