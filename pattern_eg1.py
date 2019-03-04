#WAP to print diffrent pattern

def Pattern1(n):
    print 'Pattern 1:'
    for i in range(1,n+1):
        for _ in range(1,i+1):
            print '*',
        print('')

def Pattern2(n):
    print 'Pattern 2:'
    for i in range(1,n+1):
        for _ in range(1,n-i+1):
            print ' ',      #print(' ',end='')
        for _ in range(1,i+1):
            print '*',
        print(' ')

def Pattern3(n):
    print 'Pattern 3:'
    for i in range(1,n+1):
        for _ in range(1,n-i+1):
            print ' ',
        for _ in range(1,i*2):
            print '*',
        print(' ')

def Pattern4(n):
    print 'Pattern 4:'
    for i in range(1,n+1):
        var=i
        for _ in range(1,n-i+1):
            print ' ',
        for j in range(1,i*2):
            print var,
            if j<i:
                var=var-1
            else:
                var=var+1
        print(' ')

        
def main():
    num=input('Enter number of rows:')
    Pattern1(num)
    Pattern2(num)
    Pattern3(num)
    Pattern4(num)
    

if __name__ == '__main__':
    main()

'''
= RESTART: C:/Users/Admin/Desktop/Python_2019/patterns/cw_2_2/pattern_eg1.py =
Enter number of rows:4
Pattern 1:
* 
* * 
* * * 
* * * * 
Pattern 2:
      *  
    * *  
  * * *  
* * * *  
Pattern 3:
      *  
    * * *  
  * * * * *  
* * * * * * *  
Pattern 4:
      1  
    2 1 2  
  3 2 1 2 3  
4 3 2 1 2 3 4  
>>> 
'''
