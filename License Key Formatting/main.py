#License Key Formatting

'''
Input: S = “5F3Z-2e-9-w”, K = 4
Output: “5F3Z-2E9W”
Explanation: The string S has been split into two parts,  
each part has 4 characters. 
Note that two extra dashes are not needed and can be removed.

Input: S = “2-5g-3-J”, K = 2
Output: “2-5G-3J”
Explanation: The string s has been split into three parts,  
each part has 2 characters except the first part 
as it could be shorter as mentioned above
'''

string=input("Enter a key:")    #enter a key with "-" separated
k=int(input("Enter a number:"))

key=""
for i in string:
    if i=="-":
        continue
    else:
        key+=i 
val=k
ans=""
for i in range(len(key)-1,-1,-1):
    if val==0:
        val=k
        ans+="-"
    ans+=key[i] 
    val-=1

answer=ans[::-1].upper()
print(answer)


