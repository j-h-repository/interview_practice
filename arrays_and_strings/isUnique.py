
#  Implement an algorithm to determine 
#  if a string has all unique characters. 
#  What if you cannot use additional data structures?

'''
-if the string is longer than 26 characters (exlcuding spaces)

-sort the array and check for repeats using a loop


'''

def isUnique(word):
    placeHolder = ""
    theLatter = ""

    if len(word) > 26:
        return "not a unique set of characters"
    
    else:
        for char in range(len(word)):
            if word[char].isalpha(): #check if the current char is a space or a letter
                placeHolder = word[char]
                latter = word[char+1:]

                if placeHolder in latter:
                    return "encountered a duplicate character: " + placeHolder

    

result = isUnique("ab c a efg hi")
print(result)
