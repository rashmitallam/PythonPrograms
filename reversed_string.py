#WAP to accept a string from user and return the reversed string

'''
def ReverseString(l):
    #def ReverContainer
        if len(l) == 0:
            return ''       #return [] in case of string in form of list
        x=ReverseString(l[1:])
        return x+l[0]       #x.append(l[0])
    
def main():
    l1=input('Enter a list os elements:')
    l1=ReverseString(l1)
    print l1

if __name__ == '__main__':
    main()
'''
'''
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Lists/cw_17_2/reversed_string.py 
Enter a list os elements:'rashmi'
imhsar
>>>
'''

#WAP
def ReverseContainer(l):
    if len(l) == 0:
        if type(l) == str:
            return l
        return []
    x=ReverseContainer(l[1:])
    if type(x) == str:
        return x+l[0]
    x.append(l[0])
    return x

def main():
    l1=input('Enter a string as a list:')
    l1=ReverseContainer(l1)
    print l1

if __name__ == '__main__':
    main()
