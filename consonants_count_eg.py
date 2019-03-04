#WAP to accept a string from user and count the number of consonants in it


def ConsonantCount(s):
    c=0
    for i in s:
        #if i not in "aeiouAEIOU"
        if i not in ['a','e','i','o','u','A','E','I','O','U']:
            c +=1
    return c

def main():
    s1=input("Enter a string:")
    c=ConsonantCount(s1)
    print 'No. of consonants is '+str(c)
    

if __name__ == '__main__':
    main()


>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Funtions/cw_3feb/consonants_count_eg.py 
Enter a string:'rashmi'
No. of consonants is 4
>>> 
