#WAP to accept a number from user and check if its even or odd without using arithmetic operations

def IsEven(no):
    if((no & 1)==0):
        return True
    else:
        return False

def main():
    n=input('Enter a number:')
    if IsEven(n) == True:
        print str(n)+" is an even number"
    else:
        print str(n)+" is an odd number"


if __name__ == '__main__':
    main()

'''
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Funtions/cw_3feb/even_odd_without_arith.py 
Enter a number:67
67 is an odd number
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Funtions/cw_3feb/even_odd_without_arith.py 
Enter a number:38
38 is an even number
>>>
'''
