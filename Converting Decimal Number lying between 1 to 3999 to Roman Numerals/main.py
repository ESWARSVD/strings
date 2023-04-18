#Converting Decimal Number lying between 1 to 3999 to Roman Numerals

'''
Input : 9
Output : IX

Input : 40
Output : XL

Input :  1904
Output : MCMIV
'''

integer=int(input("Enter a number:"))

m = ["", "M", "MM", "MMM"]
c = ["", "C", "CC", "CCC", "CD", "D","DC", "DCC", "DCCC", "CM "]
x = ["", "X", "XX", "XXX", "XL", "L","LX", "LXX", "LXXX", "XC"]
i = ["", "I", "II", "III", "IV", "V","VI", "VII", "VIII", "IX"]

thousands = m[integer // 1000]
hundreds = c[(integer % 1000) // 100]
tens = x[(integer % 100) // 10]
ones = i[integer % 10]

print("Roman number:",thousands+hundreds,tens+ones)