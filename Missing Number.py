class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        sum=0
        for i in range(len(nums)):
            sum=sum+nums[i]
        total=n*(n+1)//2
        ans=total-sum
        return ans