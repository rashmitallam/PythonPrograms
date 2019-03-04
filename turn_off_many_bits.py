#WAP to accept a number from user and a start bit position to turn off from given number and number of positions after start position
#Print the number in decimal after turning off respective bit

def TurnOffManyBits(n,sp,c):
    x=2**c-1
    #x=1<<(c-1)
    print bin(x)
    x=x<<(sp-c)
    print bin(x)
    x=~x
    print bin(x)
    return n&x



def main():
    num=input("Enter a number:")
    print(bin(num))
    start_pos=input('Enter the start position of bit to turn off:')
    count=input("Enter the count of bits to be turned off after start bit:")
    res=TurnOffManyBits(num,start_pos,count)
    print res
    print bin(res)

if __name__ == '__main__':
    main()

'''
>>> 
 RESTART: C:\Users\Admin\Desktop\Python_2019\Funtions\cw_3feb\turn_off_many_bits.py 
Enter a number:1023
0b1111111111
Enter the start position of bit to turn off:6
Enter the count of bits to be turned off after start bit:3
0b111
0b111000
-0b111001
967
0b1111000111
>>> 
 RESTART: C:\Users\Admin\Desktop\Python_2019\Funtions\cw_3feb\turn_off_many_bits.py 
Enter a number:441
0b110111001
Enter the start position of bit to turn off:6
Enter the count of bits to be turned off after start bit:3
0b111
0b111000
-0b111001
385
0b110000001
>>> 
'''
