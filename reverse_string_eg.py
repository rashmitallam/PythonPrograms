#WAP to revrse string using recursion

def Length(inp_string):
    if inp_string == '':
        return 0
    return 1 + Length(inp_string[1:])

def main():
    s=input('Enter a String:')
    s1=Length(s)
    print s1

    
if __name__ =='__main__':
    main()
