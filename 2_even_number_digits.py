from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                count += 1
        return count

# Example run
if __name__ == "__main__":
    sol = Solution()
    print(sol.findNumbers([12, 345, 2, 6, 7896]))
