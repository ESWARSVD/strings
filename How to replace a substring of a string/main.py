#How to replace a substring of a string

'''
Input: S = “abababa”, S1 = “aba”, S2 = “a”
Output: aba
Explanation:
Change the substrings S[0, 2] and S[4, 6](= S1) to the string S2(= “a”) modifies the string S to “aba”. Therefore, print “aba”.

Input: S = “geeksforgeeks”, S1 = “eek”, S2 = “ok”
Output: goksforgoks
'''


def modifyString(string, string1, string2):
    
    ans = ""

    i = 0
    while i < len(string):
        k = 0

        if string[i] == string1[k] and i + len(string1) <= len(string):
            j = i
 
        
            while j < i + len(string1) and string[j] == string1[k]:
                k += 1
                j += 1
 
            
            if j == i + len(string1):
                ans += string2
                i = j - 1
 
        
            else:
                ans += string[i]
        else:
            ans += string[i]
        i += 1
 
    
    print(ans)
 

String = input("Enter a string:")
string1 = input("Enter replace string:")
string2 = input("Enter replaced string:")
modifyString(String, string1, string2)


