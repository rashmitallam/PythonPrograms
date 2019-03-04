#WAP to add 2/3/4/5 integers
#Default arguments must be trailing

def add(a,b,c=0,d=0,e=0):
    return a+b+c+d+e

def mul(a,b,c=1,d=1,e=1):
    return a*b*c*d*e


def main():
    s1=add(10,20)
    print s1
    s2=add(1,2,3)
    print s2
    s3=add(12,34,45,1)
    print s3
    s4=add(1,2,3,4,5)
    print s4

    p1=mul(2,10)
    print p1
    p2=mul(10,4,5)
    print p2
    p3=mul(2,4,10,10)
    print p3
    p4=mul(10,3,6,2,0)
    print p4

if __name__ == '__main__':
    main()


'''
>>> 
= RESTART: C:/Users/Admin/Desktop/Python_2019/Funtions/cw_3feb/add_5nums.py =
30
6
92
15
20
200
800
0
>>>
'''
