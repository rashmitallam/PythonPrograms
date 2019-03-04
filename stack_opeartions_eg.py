#WAP to implement stack operations
#HW - WAP to demonstrate queue DS                                

def Push(s,e):
    if isFull(s):
        print "Stack is Full!"
    else:
        s.append(e)

def Pop(s):
    if isEmpty(s):
        print "Stack is Empty!"
    else:
        return s.pop()

def Peep(s):
    if isEmpty(s):
        print "Stack is Empty!"
    else:
        return s[-1]

def isFull(s):
    if len(s) >= 5:
        return True
    else:
        return False

def isEmpty(s):
    if len(s) == 0:
        return True
    else:
        return False

def SimulateStackOperations():
    s=input('Enter the stack elements:')
    print('Menu:')
    print('1.Push\n2.Pop\n3.Peep')
    ch = input('Enter your choice:')
    if ch == 1:
        e=input('Enter element to be pushed:')
        Push(s,e)
        print s
    elif ch == 2:
        Pop(s)
        print s
    else:
        Peep(s)
        print s
            





def main():
    SimulateStackOperations()

if __name__ == '__main__':
    main()
