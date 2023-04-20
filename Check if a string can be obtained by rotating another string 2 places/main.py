#Check if a string can be obtained by rotating another string 2 places

'''
Input: string1 = “amazon”, string2 = “azonam” 
Output: Yes 
Explanation: Rotating string1 by 2 places in anti-clockwise gives the string2.

Input: string1 = “amazon”, string2 = “onamaz” 
Output: Yes 
Explanation: Rotating string1 by 2 places in clockwise gives the string2.
'''

str1 = input("Enter a sring 1:")
str2 = input("Enter a sring 2:")

isRotated=True


if (len(str1) != len(str2)):
    isRotated=False
     
elif(len(str1) < 2):
    if str1==str2:
        isRotated=True
    else:
        isRotated=False
else:
    clockwise = ""
    anticlockwise = ""
    length = len(str2)
 
    
    anticlockwise = (anticlockwise + str2[length - 2:] +str2[0: length - 2])
     
    clockwise =clockwise + str2[2:] + str2[0:2]
    if (str1==clockwise) or (str1==anticlockwise):
        isRotated=True 
    else:
        isRotated=False
 


if isRotated:

    print("Yes") 
else:
    print("No")