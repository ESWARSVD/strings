#Count Substrings with equal number of 0s, 1s and 2s

'''
Input: str = “0102010”
Output:  2
Explanation: Substring str[2, 4] = “102” and substring str[4, 6] = “201” has equal number of 0, 1 and 2

Input: str = “102100211”
Output: 5

'''


string=input("Enter a string:")  #Enter string with "0","1","2"s 
arr=[]

for str1 in range(len(string)-1):
    for str2 in range(str1+1,len(string)):
        arr.append(string[str1:str2])
count=0
for str3 in arr:
    countzero=0
    countone=0
    counttwo=0
    for str4 in str3:
        if str4=="0":
            countzero+=1
        if str4=="1":
            countone+=1
        if str4=="2":
            counttwo+=1
    if (countzero==countone) and (countone==counttwo):
        count+=1


print(count)
