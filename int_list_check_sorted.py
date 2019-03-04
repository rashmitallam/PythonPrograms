#WAP to accept a list of intergers from user and check id it is already sorted or not

def IsSorted(l):
    i=0
    while i < len(l):
        j=i+1
        while j in len(l):
            if i<j:
                i=j
                j += 1
            else:
                return False
        return True
    
            


def main():
    l=input('Enter a list of integers:')
    s=IsSorted(l)
    if s == 'True':
        print('List is already sorted')
    else:
        print('List in not sorted')
    

if __name__ == '__main__':
    main()
    
