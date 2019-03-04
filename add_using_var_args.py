#Add function with variable arguments



def add(*args):
    print(type(args))
    print(args)
    res=0
    for i in args:
        res=res+i
    return res

def main():
    print(add(1,2))
    print(add(100,20,30,40))


if __name__ == '__main__':
    main()

'''
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Funtions/cw_3feb/add_using_var_args.py 
<type 'tuple'>
(1, 2)
3
<type 'tuple'>
(100, 20, 30, 40)
190
>>> 
'''
