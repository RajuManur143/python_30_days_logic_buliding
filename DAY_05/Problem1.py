class Solution:


    def sumOfArray(self,nums):

        sum = 0

        for index in range(0,len(nums)):
            sum += nums[index]
            
        return sum
    
### invoke
Result = Solution()

nums = [1,2,3,4,5]

sumOfNumber = Result.sumOfArray(nums)

print("sum of array is = ",sumOfNumber)