class Solution:
    
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        a = [2, 3, 5]
        for i in a:
            # print("{} / {} = {}".format(num, i, num//i))
            while num % i == 0:
                print("{} / {} = {}".format(num, i, num//i))
                num = num // i
            
        print("{}".format(num))
        if num == 1 or num == -1:
            return True
        else: 
            return False

a = Solution()
print("{}".format(a.isUgly(-2147483648))) #false