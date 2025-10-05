class Solution:

    def calulator(self):

        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the Second number:"))

        choice = input("Enter the what operation you want: ")

        match choice:
            case "+":
                print("Addition is =",num1 + num2)

            case "-":
                print("Substraction is =",num1 - num2)

            case "*":
                print("Multiplication is =",num1 * num2)

            case "/":
                print("Division is = ",num1/num2)

            case "%":
                print("Modulus is = ",num1%num2)


### Invoke
Result = Solution()

Result.calulator()
