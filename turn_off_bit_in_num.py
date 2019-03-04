#WAP to accept a number from user and a bit position to turn off from given number.
#Print the number in decimal after turning off respective bit

def TurnOffBit(n,p):
    x=1
    x=x<<(p-1)
    x=~x
    return n&x

def main():
    num=input("Enter a number:")
    pos=input("Enter the position to be turned off:")
    res=TurnOffBit(num,pos)
    print res
    

if __name__ == '__main__':
    main()

'''
RESTART: C:/Users/Admin/Desktop/Python_2019/Funtions/cw_3feb/turn_off_bit_in_num.py 
Enter a number:16
Enter the position to be turned off:5
0
>>>
RESTART: C:/Users/Admin/Desktop/Python_2019/Funtions/cw_3feb/turn_off_bit_in_num.py 
Enter a number:16
Enter the position to be turned off:4
16
>>> 
'''
