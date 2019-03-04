#Python Program to Check Whether a String is Palindrome or Not

str1='malayalamadads'

#str1 = str1.casefold()

rev_str1=reversed(str1)

if list(str1) == list(rev_str1):
    print('Palindrome')
else:
    print('Not a Palindrome')
    
