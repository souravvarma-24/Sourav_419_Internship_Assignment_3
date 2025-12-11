class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        summ = 0

        for d in str(n):
            digit = int(d)
            product *= digit
            summ += digit

        return product - summ

# Example run
if __name__ == "__main__":
    sol = Solution()
    print(sol.subtractProductAndSum(234))
