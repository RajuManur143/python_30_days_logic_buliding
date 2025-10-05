class Solution:

    def MultiplicationTable(self,num):

        for index in range(1,11,1):
            Result = num * index
            print(f"{num}*{index} = {Result}",end="")
            print("\n")


### Invoke
Result = Solution()

num = int(input("Enter the number = "))

Result.MultiplicationTable(num)
