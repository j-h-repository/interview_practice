'''
Rotate Matrix: 
Given an image represented by an NxN matrix, 
where each pixel in the image is 4 bytes, 
write a method to rotate the image by 90 degrees. 

Can you do this in place?

NOTES DOWN BELOW
'''



def rotateByNinety(picture):
    newRotation=[]
   
    for row in range(len(picture)):
        
        if len(newRotation)<row+1:
            newRotation.append([])
       
        for newRow in range(len(picture[row])):
           
            newRotation[row].append(picture[newRow][row])
        newRotation[row].reverse()
        print("new photo row ", row+1, ": ",newRotation[row])
        

def createPhoto(size):
    parentArr = []
    for num in range(size):
        parentArr.append([])
        for bit in range(size):
            parentArr[num].append(bit+1)
        print("parent photo row ", num+1, ": ",parentArr[num])
    return parentArr


photo = createPhoto(7) #CREATE A PHOTO HERE

rotatedPhoto= rotateByNinety(photo) #THE ROTATED PHOTO IS STORED HERE


'''
RULES
if we have a perfectly square matrix (e.g. 6 rows and columns)

if n is odd, we never touch the parentArray[n-1/2] nor the subarray[n-1/2] element
    [2,2,2,2,2]
    [2,1,1,1,2]
    [2,1,0,1,2]
    [2,1,1,1,2]
    [2,2,2,2,2]


if n is 2 we only do one rotation, since there are only perimeter elements
if n is 3, we do 1 rotations, since 
if n is 4, we do 2 rotations
if n is 5, we do 2 rotations

if n is 12 --> since n i even, we do n/2 rotations
if n is 17 --> since n is odd, we do n-1/2 rotations



'''
Operation

e.g using this matrix (5x5)

    [2,2,2,2,2]
    [2,1,1,1,2]
    [2,1,0,1,2]
    [2,1,1,1,2]
    [2,2,2,2,2]

we can work our way out
we would probably need to copy the bits from the image individually
then generate another photo incrementally

capture each row

one row will be come a column

using brute force

time complexity is n^2

'''