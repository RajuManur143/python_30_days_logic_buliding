




class Solution:

    def isDivisibleByFive(self,num):

        if num % 5 == 0:

            print(f"{num} is divisible by 5")

        else:

            print(f"{num} is not divisible by 5")

### Invoke

Result = Solution()

num = int(input("Enter the numbers :"))

Result.isDivisibleByFive(num)

