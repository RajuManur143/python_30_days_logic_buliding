class Solution(object):

    def reverseOrder(self,num):

        for index in range(len(num)-1,-1,-1):
            print(f'{num[index]}',end=" ")
            


### Invoke
Result = Solution()

num = [1,2,3,4]

Result.reverseOrder(num)