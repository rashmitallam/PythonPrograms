#WAP to remove all occurences of given data from a list

def RemoveAllOccurences(l,c):
    while(c in l):
        l.remove(c)
#no need to return the value, since container itself is getting modified

def main():
    l=input('Enter a list:')
    c=input('Enter element that needs to removed from list:')
    RemoveAllOccurences(l,c)
    print l

if __name__ == '__main__':
    main()

'''
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Lists/cw_16_2/remove_all_occurnces.py 
Enter a list:[1,2,3,4,2,2,5,2,5,6,2,6,2,6]
Enter element that needs to removed from list:2
[1, 3, 4, 5, 5, 6, 6, 6]
>>> 
'''
'''
>>> 
 RESTART: C:\Users\Admin\Desktop\Python_2019\Lists\cw_16_2\remove_all_occurnces.py 
Enter a list:[1,2,4,234,6,1,1,1,2,'sad',1,"asd",1]
Enter element that needs to removed from list:1
[2, 4, 234, 6, 2, 'sad', 'asd']
>>>
'''
