#Converting Roman Numerals to Decimal lying between 1 to 3999
'''
Input: IX
Output: 9
IX is a Roman symbol which represents 9 

Input: XL
Output: 40
XL is a Roman symbol which represents 40

Input: MCMIV
Output: 1904
M is a thousand, 
CM is nine hundred and 
IV is four

'''

def roman(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1
input=input("Enter a roman number:")  
ans = 0
i = 0
 
while (i < len(input)):
 
        
    str_1 = roman(input[i])
 
    if (i + 1 < len(input)):
 
         
        str_2 = roman(input[i + 1])
 
            
        if (str_1 >= str_2):
            ans = ans + str_1
            i = i + 1
        else:
            ans = ans + str_2 - str_1
            i = i + 2
    else:
        ans = ans + str_1
        i = i + 1

print(ans)