class Solution:
    def superPow(self, a: int, b: [int]) -> int:
        for p in b[::-1]:
            print(p)
        return 1

a = Solution()
print("{}".format(a.superPow(2, [1, 2])))