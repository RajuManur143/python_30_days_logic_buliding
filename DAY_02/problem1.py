class Solution:

    def isEven_or_Odd(self,num):

        
        
        
        if (num % 2 == 0):
            return True
        
        else:
            return False




### invoke
Result = Solution()

num = int(input("Enter the number: "))

print(Result.isEven_or_Odd(num))