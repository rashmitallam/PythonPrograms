#WAP to accept a sentence from user and return dict containing count of each characters occuring in it

def DictChars(s1):
    res=dict()

    for ch in s1:
        if res.get(ch) != None:
            res[ch] += 1
        else:
            res[ch] = 1
    
    return res

def main():
    s=input('Enter a sentence:')
    s2=DictChars(s)
    print s2

    for x in s2:
        print(x,s2[x])

if __name__ == '__main__':
    main()


'''
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Dictionary/count_char_in_sentence.py 
Enter a sentence:'India is my country'
{'a': 1, ' ': 3, 'c': 1, 'd': 1, 'I': 1, 'm': 1, 'o': 1, 'n': 2, 'i': 2, 's': 1, 'r': 1, 'u': 1, 't': 1, 'y': 2}
>>>
'''
'''
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Dictionary/count_char_in_sentence.py 
Enter a sentence:'India is my country'
{'a': 1, ' ': 3, 'c': 1, 'd': 1, 'I': 1, 'm': 1, 'o': 1, 'n': 2, 'i': 2, 's': 1, 'r': 1, 'u': 1, 't': 1, 'y': 2}
('a', 1)
(' ', 3)
('c', 1)
('d', 1)
('I', 1)
('m', 1)
('o', 1)
('n', 2)
('i', 2)
('s', 1)
('r', 1)
('u', 1)
('t', 1)
('y', 2)
>>> 
'''
