class Solution:

    def isvowel(self,character):

        if (character == "a" or 
            character == "e" or 
            character == "i" or 
            character == "o" or 
            character == "u"):
            print("This is vowel ",character)
        
        elif (character == "A" or 
              character == "E" or 
              character == "I" or 
              character == "O" or 
              character == "U"):
            print("This is the vowel ",character)

        else:
            print("This is not vowel ",character)

        return
            

### invoke
Result = Solution()

character = input("Enter the Character ")

Result.isvowel(character)