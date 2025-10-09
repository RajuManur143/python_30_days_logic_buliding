class Solution:

    def PrintGrid(self,row,col):

        for rows in range(0,row):
            for cols in range(0,col):
                print("*",end=" ")
            print("\n")




### Invoke
Result = Solution()

row = 4
col = 4

Result.PrintGrid(row,col)