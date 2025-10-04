class Solution:

    def iscircleTriangle(self,num,base,height):

        PI = 3.14

        radius = PI*num*num
        print("Area  of circle is = ",radius)

        Triangle = 0.5*base*height
        print("Area of Triangle is = ",Triangle)


### Invoke
Result = Solution()

num = 5

base = 10

height = 4

Result.iscircleTriangle(num,base,height)
