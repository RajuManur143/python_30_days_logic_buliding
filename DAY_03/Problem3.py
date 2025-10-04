class Solution:

    def findReminderQuoteint(self,dividend,divisor):

        Reminder = dividend % divisor
        Quotient = dividend//divisor

        print("Reminder is  = ",Reminder)
        print("Quotient is = ",Quotient)




### Invoke
Result = Solution()

dividend = 22
divisor = 7

Result.findReminderQuoteint(dividend,divisor)