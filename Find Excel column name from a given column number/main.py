#Find Excel column name from a given column number
'''
Input          Output
 26             Z
 51             AY
 52             AZ
 80             CB
 676            YZ
 702            ZZ
 705            AAC
'''

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
def number(num):
    if num < 26:
        return alpha[num-1]
    else:
        q, r = num//26, num % 26
        if r == 0:
            if q == 1:
                return alpha[r-1]
            else:
                return number(q-1) + alpha[r-1]
        else:
            return number(q) + alpha[r-1]
 
num=int(input("Enter a number:"))

print("output:",number(num))
