Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:40:30) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=== RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/string_slicing.py ===
('str =', 'programiz')
('First character = ', 'p')
('Last Character = ', 'z')
('str[1:5] = ', 'rogr')
('str[5:-2] = ', 'am')
>>> string = 'Rashmi'
>>> string[15]

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    string[15]
IndexError: string index out of range
>>> string[1.5]

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    string[1.5]
TypeError: string indices must be integers, not float
>>> str='rashmi'
>>> str[2]='a'

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    str[2]='a'
TypeError: 'str' object does not support item assignment
>>> str='Python'
>>> print(str)
Python
>>> str
'Python'
>>> del str[1]

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    del str[1]
TypeError: 'str' object doesn't support item deletion
>>> del str
>>> str
<type 'str'>
>>> string1='rashmi'
>>> del string[2]

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    del string[2]
TypeError: 'str' object doesn't support item deletion
>>> del string1[2]

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    del string1[2]
TypeError: 'str' object doesn't support item deletion
>>> del string1
>>> string1

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    string1
NameError: name 'string1' is not defined
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/string_concat_repeat.py 
('str1 + str2 = ', 'RashmiTallam')
('str1*3 = ', 'RashmiRashmiRashmi')
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/string_concat_repeat.py 
('str1 + str2 = ', 'RashmiTallam')
('str1*3 = ', 'RashmiRashmiRashmi')
HelloWorld
HelloooWorld!!
>>> 
== RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/string_iteration.py ==

Traceback (most recent call last):
  File "C:/Users/Admin/Desktop/Python_2019/Strings/string_iteration.py", line 5, in <module>
    if(letter == l):
NameError: name 'l' is not defined
>>> 
== RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/string_iteration.py ==
(3, ' letters found!')
>>> 
== RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/string_iteration.py ==
(3, 'letters found')
>>> a in 'program'

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a in 'program'
NameError: name 'a' is not defined
>>> 'a' in 'program'
True
>>> 'at' not in 'bat'
False
>>> str = 'cold'
>>> list(enumerate(str))
[(0, 'c'), (1, 'o'), (2, 'l'), (3, 'd')]
>>> len(str)
4
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/string_escape_sequence.py 
He said,"What's there?"
He said, "What's there?"
He said,"What's there?"
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/string_escape_sequence.py 
He said, "What's there?"
He said, "What's there?"
He said, "What's there?"
>>> print("C:\\Python\\Lib")
C:\Python\Lib
>>> print("This is printed \n in two lines")
This is printed 
 in two lines
>>> print('This is \x48\x45\x58 representation')
This is HEX representation
>>> print(r'This is \x48\x45\x58 representation')
This is \x48\x45\x58 representation
>>> print(R'This is \x48\x45\x58 representation')
This is \x48\x45\x58 representation
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/strings_format_method.py 
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/strings_format_method.py 

---Default Order---
John,Bill and Sean
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/strings_format_method.py 

---Default Order---
John,Bill and Sean

---Positional Order---
Bill,John and Sean
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/strings_format_method.py 

---Default Order---
John,Bill and Sean

---Positional Order---
Bill,John and Sean

---PoKeywordsitional Order---
Sean,John and Bill
>>> 
== RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/string_formatting.py ==
Binary representation of 12 is 1100
Exponent representation: 1.566345e+03
One third is: 0.000
|butter    |  bread   |       ham|
>>> 
== RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/string_formatting.py ==
Binary representation of 12 is 1100
Exponent representation: 1.566345e+03
One third is: 0.000
|butter|  bread   |       ham|
>>> 
== RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/string_formatting.py ==
Binary representation of 12 is 1100
Exponent representation: 1.566345e+03
One third is: 0.000
|butter|  bread   |       ham|
>>> "PrOgRaMiZ".lower()
'programiz'
>>> "PrOgRaMiZ".upper()
'PROGRAMIZ'
>>> "This will split all words into a list".split()
['This', 'will', 'split', 'all', 'words', 'into', 'a', 'list']
>>> ' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string'])
'This will join all words into a string'
>>> 'Happy New Year'.find('ew')
7
>>> 'Happy New Year'.replace('Happy','Brilliant')
'Brilliant New Year'
>>> 
== RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/string_palindrome.py ==

Traceback (most recent call last):
  File "C:/Users/Admin/Desktop/Python_2019/Strings/string_palindrome.py", line 5, in <module>
    str1=str1.casefold()
AttributeError: 'str' object has no attribute 'casefold'
>>> 
== RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/string_palindrome.py ==

Traceback (most recent call last):
  File "C:/Users/Admin/Desktop/Python_2019/Strings/string_palindrome.py", line 5, in <module>
    str1 = str1.casefold()
AttributeError: 'str' object has no attribute 'casefold'
>>> 
== RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/string_palindrome.py ==

Traceback (most recent call last):
  File "C:/Users/Admin/Desktop/Python_2019/Strings/string_palindrome.py", line 5, in <module>
    str1 = str1.casefold()
AttributeError: 'str' object has no attribute 'casefold'
>>> 
== RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/string_palindrome.py ==
Not a Palindrome
>>> 
== RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/string_palindrome.py ==
Palindrome
>>> 
== RESTART: C:\Users\Admin\Desktop\Python_2019\Strings\string_palindrome.py ==
Not a Palindrome
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/remove_punc_from_string.py 
Enter a string:'Hello,World! How are you ?'
HelloWorld How are you 
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/sort_string_alphabetically.py 
Enter a sentence:What is your name

Traceback (most recent call last):
  File "C:/Users/Admin/Desktop/Python_2019/Strings/sort_string_alphabetically.py", line 3, in <module>
    str1=input("Enter a sentence:")
  File "<string>", line 1
    What is your name
                    ^
SyntaxError: unexpected EOF while parsing
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/sort_string_alphabetically.py 
Enter a sentence:'What is your name?'

Traceback (most recent call last):
  File "C:/Users/Admin/Desktop/Python_2019/Strings/sort_string_alphabetically.py", line 7, in <module>
    str1=str.sort()
AttributeError: type object 'str' has no attribute 'sort'
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/sort_string_alphabetically.py 
Enter a sentence:'What is your name'

Traceback (most recent call last):
  File "C:/Users/Admin/Desktop/Python_2019/Strings/sort_string_alphabetically.py", line 9, in <module>
    for word in str1:
TypeError: 'NoneType' object is not iterable
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/sort_string_alphabetically.py 
Enter a sentence:'What is your name'
What
is
name
your
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/sort_string_alphabetically.py 
Enter a sentence:'What is my name'
What
is
my
name
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/sort_string_alphabetically.py 
The sorted words are:
Example
Hello
Is
With
an
cased
letters
this
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/sort_string_alphabetically.py 
Enter a sentence:"Hello this Is an Example With cased letters"
Example
Hello
Is
With
an
cased
letters
this
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Strings/sort_string_alphabetically.py 
Enter a sentence:"what Is Your name ?"
?
Is
Your
name
what
>>> 
