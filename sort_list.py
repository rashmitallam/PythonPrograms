#WAP to accept an unsorted list of numbers from user and sort it

def SortList(s):
    l=len(s)
    for i in range(l-1):
        for j in range(i+1,l):
            if s[i] > s[j]:
                t=s[i]
                s[i]=s[j]
                s[j]=t


def main():
    s1=input('Enter an unsorted list:')
    SortList(s1)
    print('Sorted list:')
    print s1

if __name__ == '__main__':
    main()
