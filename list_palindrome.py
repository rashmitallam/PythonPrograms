#WAP to accept a list of integers from user and check if its palindrome or not

def isPalindrome(l):
    n=len(l)
    res=0
    for i in range(0,(n-1)/2):
        if l[i] == l[-i]:
            res=res+l[-i]
        else:
            res=res+l[i]
    if res == n:
        return True
    else:
        return False

