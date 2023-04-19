#Check if given String is Pangram or not

'''
Input: “The quick brown fox jumps over the lazy dog” 
Output: is a Pangram 
Explanation: Contains all the characters from a to z]

Input: “The quick brown fox jumps over the dog”
Output: is not a Pangram 
Explanation: Does not contain all the characters from a to z, as l, z, y are missing

'''


string=input("Enter a sentence:")
string=string.upper()
result=True
for num in range(1,27):
    if chr(64+num) in string:
        continue
    else:
        result=False 
        break 


if result:
    print("this sentence is a pangram")
else:
    print("this sentence is not a pangram")
    