#Shortest Common supersequence
'''
Input:   str1 = "geek",  str2 = "eke"
Output: 5
Explanation: 
String "geeke" has both string "geek" 
and "eke" as subsequences.

Input:   str1 = "AGGTAB",  str2 = "GXTXAYB"
Output:  9
Explanation: 
String "AGXGTXAYB" has both string 
"AGGTAB" and "GXTXAYB" as subsequences.
'''

 
def supersequence(X, Y, m, n):
    if (not m):
        return n
    if (not n):
        return m
 
    if (X[m - 1] == Y[n - 1]):
        return 1 + supersequence(X, Y, m - 1, n - 1)
 
    return 1 + min(supersequence(X, Y, m - 1, n),
                   supersequence(X, Y, m, n - 1))
 
 

str1 = input("Enter string1:")

str2 = input("Enter string2:")
print("Length of the shortest supersequenceuence is %d"
      % supersequence(str1, str2, len(str1), len(str2)))