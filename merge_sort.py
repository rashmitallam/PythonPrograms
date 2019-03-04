#WAP to implement merge sort

def BubbleSort(l):
    i=0
    for i in range(len(l)):
        already_sorted=True
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                t=l[j]
                l[j]=l[j+1]
                l[j+1]=t

def MergeSort(a,b):
    i=0
    c=[]
    j=0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c.extend(a[i:])
    else:
        c.extend(b[j:])
    return c


def main():
    a=input('Enter 1st list:')
    BubbleSort(a)
    print a
    b=input('Enter 2nd list:')
    BubbleSort(b)
    print b
    c=MergeSort(a,b)
    print c

if __name__ == '__main__':
    main()


'''
>>> 
== RESTART: C:/Users/Admin/Desktop/Python_2019/Lists/cw_17_2/merge_sort.py ==
Enter 1st list:[5,3,1]
[1, 3, 5]
Enter 2nd list:[2,8,4,9]
[2, 4, 8, 9]
[1, 2, 3, 4, 5, 8, 9]
>>> 
'''
'''
>>> 
== RESTART: C:/Users/Admin/Desktop/Python_2019/Lists/cw_17_2/merge_sort.py ==
Enter 1st list:[1,4,7]
[1, 4, 7]
Enter 2nd list:[1,2]
[1, 2]
[1, 1, 2, 4, 7]
>>> 
'''
