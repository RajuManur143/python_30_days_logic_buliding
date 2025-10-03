class Solution:

    def find_the_largest_number_among_two_integers(self,num1,num2):


        if num1 >= num2:
            return num1
        
        else:
            return num2




## Invoke
Result = Solution()
num1 = int(input("Enter the number1:"))
num2 = int(input("Enter the number2:"))

largerst = Result.find_the_largest_number_among_two_integers(num1,num2)
print("largest number is among two numbers is = ",largerst)

