import sys

class Solution:
    def find_the_size_of_variables(self):

        a = 10
        b = 10.22
        c = "10"
        d = True
        e = "Raju"
        f = [1,2,3,4]
        g = {1:"one" , 2: "Two"}


        print("size of int = ",sys.getsizeof(a))
        print("size of float = ",sys.getsizeof(b))
        print("size of string = ",sys.getsizeof(c))
        print("size of boolen = ",sys.getsizeof(d))
        print("size of string_char = ",sys.getsizeof(e))
        print("size of list = ",sys.getsizeof(f))
        print("size of dictionary = ",sys.getsizeof(g))

## Invoke
Result = Solution()
Result.find_the_size_of_variables()