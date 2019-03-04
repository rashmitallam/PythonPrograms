#WAP to accept a list from user and print it element by element in reverse order using recursion

def ReverseListPrint(l):
        if len(l) == 0:
            return 0
        ReverseListPrint(l[1:])
        print(l[0])
    
def main():
    l1=input('Enter a list os elements:')
    ReverseListPrint(l1)

if __name__ == '__main__':
    main()

>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Lists/cw_17_2/reverse_list_recursion.py 
Enter a list os elements:[1,7,9,6]
6
9
7
1
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Lists/cw_17_2/reverse_list_recursion.py 
Enter a list os elements:'Rashmi'
i
m
h
s
a
R
>>> 
