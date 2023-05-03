'''
There are three types of edits that can be performed on strings: 
insert a character, remove a character, or replace a character. 

Given two strings, write a function to check if they are one edit (or zero edits) away.

EXAMPLE
pale, ple -> true 
pales, pale -> true 
pale, bale -> true 
pale, bake -> false
'''


def checkEdits(string):
    before = string.split(", ")[0]
    after = string.split(", ")[1]

    
    changes =0#store change detection as an integer starting at 0
    oneOrLessChange=True#default False
    #grab second string
    for char in range(len(after)):#interate through
        if(after[char] not in before):#on each iteration, check if char in string2 is not included in string1
            changes=changes+1# increment changes
            if changes>1:#if more than one change is detected
                oneOrLessChange = False
                return ('one change or less: ' + str(oneOrLessChange))#return "1 or less change" to false
    #return 
    return ('one change or less: ' + str(oneOrLessChange))


result = checkEdits('pale, bake')
print(result)