#Find largest word in dictionary by deleting some characters of given string

'''
Input : list = ["ale", "apple", "monkey", "plea"]   
str = "abpcplea"  
Output : apple 

Input  : list = ["pintu", "geeksfor", "geeksgeeks", " forgeek"]
str = "geeksforgeeks"
Output : geeksgeeks

Giving a dictionary and a string str, find the longest 
string in dictionary which can be formed by deleting some characters of the given str. 
'''

given_list=input("Enter a list:").split(",")  #enter , separated strings
string=input("Enter string:")

count_list=[]
for strings in given_list:
    dict_string=string 
    count=0
    for str in strings:
        if str in dict_string:
            count+=1
            dict_string.strip(str)
    count_list.append(count)

maximum=max(count_list)
index=count_list.index(maximum)

print("largest word:",given_list[index])