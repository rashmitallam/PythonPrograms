#WAP to generate a pattern

def Pattern1(n):
    for i in range(1,n+1):
        var=i
        for j in range(1,i+2):
            print var,
            var *= 2
        print('')


def main():
    Pattern1(4)

if __name__ == '__main__':
    main()


'''
>>> 
== RESTART: C:/Users/Admin/Desktop/Python_2019/patterns/cw_9_2/pattern3.py ==
1 2 
2 4 8 
3 6 12 24 
4 8 16 32 64 
>>>
'''
