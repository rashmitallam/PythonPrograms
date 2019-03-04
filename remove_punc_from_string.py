#Python Program to Remove Punctuations From a String

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

str1 = input("Enter a string:")

op_str = ""

for char in str1:
    if char not in punctuations:
        op_str = op_str + char

print(op_str)
