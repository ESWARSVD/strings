#Check if two strings are k-anagrams or not

'''
Input:  str1 = "anagram" , str2 = "grammar" , k = 3
Output:  Yes
Explanation: We can update maximum 3 values and 
it can be done in changing only 'r' to 'n' 
and 'm' to 'a' in str2.

Input:  str1 = "geeks", str2 = "eggkf", k = 1
Output:  No
Explanation: We can update or modify only 1 
value but there is a need of modifying 2 characters. 
i.e. g and f in str 2.
'''


MAX_CHAR = 26
string1=input("Enter string 1:")
string2=input("Enter string 2:")
k=int(input("Enter max changes:"))

n = len(string1);
if (len(string2) != n):
    result=False
else:

 
    str = [0]*(MAX_CHAR)
    for i in range(n):
        str[ord(string1[i]) - ord('a')]+=1
 
    count = 0
    result=True
    for i in range(n):
        if (str[ord(string2[i]) - ord('a')] > 0):
            str[ord(string2[i]) - ord('a')]-=1
        else:
            count+=1
 
        if (count > k):
            result=False
            break
if result:
    print("Yes")
else:
    print("NO")
