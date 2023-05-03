'''
Write a method to replace all spaces in a string with '%20'. 
You may assume that the string has sufficient space at the 
end to hold the additional characters,and that you are given 
the "true" length of the string. 

(Note: If implementing in Java,please use a character array so that you can perform this operation in place.)

EXAMPLE
Input: "Mr John Smith ", 
Output: "Mr%20John%20Smith"
'''


def urlIfy(string):
    holding = [] #a place to hold the string until the loop is complete
    arr = string.split() #splits the current string by white space

    for word in range(len(arr)):
        if word == len(arr)-1: #if we come across the last item in "arr", we don't want to add %20
            holding.append(arr[word]) #so we only add the last string element alone
        else:
            holding.append(arr[word]+"%20") #otherwise, we add the string at arr[index] and %20
       
    return "".join(holding)

url = urlIfy("peace be with you")

print(url)