from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            smaller = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    smaller += 1
            result.append(smaller)
        return result

# Example run
if __name__ == "__main__":
    sol = Solution()
    print(sol.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
