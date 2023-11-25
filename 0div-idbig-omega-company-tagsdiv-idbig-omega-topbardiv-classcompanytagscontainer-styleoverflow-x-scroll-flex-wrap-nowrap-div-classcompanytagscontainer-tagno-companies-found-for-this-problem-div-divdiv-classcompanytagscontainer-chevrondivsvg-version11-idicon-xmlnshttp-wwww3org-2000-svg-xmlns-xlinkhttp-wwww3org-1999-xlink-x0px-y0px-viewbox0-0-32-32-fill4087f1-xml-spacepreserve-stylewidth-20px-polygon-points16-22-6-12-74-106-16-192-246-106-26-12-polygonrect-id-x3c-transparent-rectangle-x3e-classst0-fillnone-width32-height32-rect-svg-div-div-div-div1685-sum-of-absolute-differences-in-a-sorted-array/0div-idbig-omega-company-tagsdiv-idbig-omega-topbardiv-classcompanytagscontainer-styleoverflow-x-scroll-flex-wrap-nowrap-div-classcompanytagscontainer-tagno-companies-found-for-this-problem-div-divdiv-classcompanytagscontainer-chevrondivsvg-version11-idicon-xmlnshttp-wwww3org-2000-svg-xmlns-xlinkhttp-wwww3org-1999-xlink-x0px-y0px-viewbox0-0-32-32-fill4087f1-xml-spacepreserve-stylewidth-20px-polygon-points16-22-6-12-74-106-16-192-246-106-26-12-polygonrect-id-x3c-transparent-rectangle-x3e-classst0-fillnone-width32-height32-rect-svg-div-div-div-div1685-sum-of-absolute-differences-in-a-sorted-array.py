class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        res=[]
        leftSum=0
        rightSum=sum(nums)

        for i in range(len(nums)):

            temp= (nums[i]*i - leftSum) + (rightSum - nums[i]*(len(nums)-i) )
            leftSum+=nums[i]
            rightSum-=nums[i]
            res.append(temp)
        
        return res