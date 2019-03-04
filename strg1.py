#WAP to accept 2 strings from user and swap their 1st two characters

str1=input('Enter 1st string:')
str2=input('Enter 2nd string:')

#Slicing 1st 2 characters of both strings and swapping their positions
str3= str2[:2]+str1[2:]+' '+str1[:2]+str2[2:]

print(str3)

