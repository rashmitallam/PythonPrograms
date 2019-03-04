#WAP to accept a number from user and return a dict of squares from 1 to that number


def GenerateSquares(n):
    res=dict()

    for i in range(1,n+1):
        res[i] = i*i
    return res
    
def main():
    n=input('Enter a number:')
    s=GenerateSquares(n)
    print s


if __name__ == '__main__':
    main()

'''
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Dictionary/cw_2_3/squares_dict.py 
Enter a number:10
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
>>>
'''
