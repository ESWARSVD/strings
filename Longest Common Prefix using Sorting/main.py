#Longest Common Prefix using Sorting
'''
Input: {“geeksforgeeks”, “geeks”, “geek”, “geezer”}
Output: “gee”

Input: {“apple”, “ape”, “april”}
Output: “ap”
'''

strings_array=input("Enter string list:").split(",")  # Enter , seperated words
common=""
strings_array.sort()
length=len(strings_array)

if length==0:
    print("")
elif length==1:
    print(strings_array[0])
else:
    n=0
    min_len=min(len(strings_array[0]),len(strings_array[-1]))
    len=0
    while len<min_len:
        string=strings_array[0][len]
        for str_1 in range(length):
            if strings_array[str_1][len]==string:
                continue
            else:
                len=min_len
                break
        n+=1
        len+=1
if n==0:
    print("No common word")
else:
    print(strings_array[0][:n-1])

            
