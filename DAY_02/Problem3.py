


class Solution:

    def isMultiple(self,num):

        if num % 7 == 0:
            print(f"{num} is Multiple of 7")

        else:
            print(f"{num} is not Multiple of 7")



#### Invoke
Result = Solution()

num = int(input("Enter the number :"))

Result.isMultiple(num)