# sorted squared nums 
class Solution(object):
    def sortedSquares(self, nums):

        n=len(nums)
        res=[0]*n
        for i in range (n):
            res[i]=nums[i]**2
        res.sort()
        return print(res)
sol=Solution()
sol.sortedSquares([-7,-3,2,3,11])