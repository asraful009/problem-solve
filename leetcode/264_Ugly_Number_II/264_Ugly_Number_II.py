class Solution:
    a = [2, 3, 5]
    nset = [1]
    def __init__(self) :
        for j in self.nset:
            if len(self.nset) == 9000:
                break
            # print(self.nset)
            for k in self.a:
                # print("{}*{} = {}".format(j, k, j*k))
                if j*k not in self.nset:
                    self.nset.append(j*k)
        self.nset.sort()
        #print(self.nset)
        
    def nthUglyNumber(self, n: int) -> int:
        return self.nset[n-1]

a = Solution()
print("{}".format(a.nthUglyNumber(1352))) #402653184