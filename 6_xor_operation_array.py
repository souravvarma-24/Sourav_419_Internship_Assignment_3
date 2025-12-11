class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor_val = 0
        for i in range(n):
            xor_val ^= (start + 2*i)
        return xor_val

# Example run
if __name__ == "__main__":
    sol = Solution()
    print(sol.xorOperation(5, 0))
