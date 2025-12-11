from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        freq = {}

        for n in nums:
            if n in freq:
                pairs += freq[n]
                freq[n] += 1
            else:
                freq[n] = 1

        return pairs

# Example run
if __name__ == "__main__":
    sol = Solution()
    print(sol.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
