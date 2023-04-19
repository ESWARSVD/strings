#Minimum number of deletions to make a string palindrome
'''
Input : aebcbda
Output : 2
Remove characters 'e' and 'd'
Resultant string will be 'abcba'
which is a palindromic string

Input : geeksforgeeks
Output : 8

'''

def countofdelete(string):
    n = len(string)
  
    L = [[0 for x in range(n)]for y in range(n)]
  
    for i in range(n):
        L[i][i] = 1
  
    for cl in range( 2, n+1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if (string[i] == string[j] and cl == 2):
                L[i][j] = 2
            elif (string[i] == string[j]):
                L[i][j] = L[i + 1][j - 1] + 2
            else:
                L[i][j] = max(L[i][j - 1],L[i + 1][j])
  
    return L[0][n - 1]
  
def minimumNumberOfDeletions( string):
 
    n = len(string)
  
   
    l = countofdelete(string)
  
    return (n - l)


     
string = input("Enter a stringing:")
print( "Minimum number of deletions = ", minimumNumberOfDeletions(string))