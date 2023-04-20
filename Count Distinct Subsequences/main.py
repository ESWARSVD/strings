#Count Distinct Subsequences

'''
Input  : str = "gfg"
Output : 7
The seven distinct subsequences are "", "g", "f",
"gf", "fg", "gg" and "gfg" 

Input  : str = "ggg"
Output : 4
The four distinct subsequences are "", "g", "gg"
and "ggg"
'''
#using python libraries

from itertools import combinations

string=input("Enter a string:")
substring=[]
for str1 in range(1,len(string)+1):
    sub=combinations(string,str1)
    for i in sub:
        substring.append(i)
    
    
#uniqe substrings
substring=set(substring)
substring=list(substring)
#print count of substrings

print(len(substring)+1)