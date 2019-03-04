#WAP to count number of bits in input

def CountOne(no):
    if no == 0:
        return 0
    return 1 + CountOne(no&(no-1))


def main():
    n=input("Enter a number:")
    print bin(n)
    c=CountOne(n)
    print "Number of bits = "+ str(c)

if __name__ == '__main__':
    main()

>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Recursion/cw_16_2/count_no_of_bits.py 
Enter a number:180
0b10110100
Number of bits = 4
>>> 
