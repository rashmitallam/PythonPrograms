#WAP to make use of Variable Arguments Dictionary

def VariableArgsDictionary(a,b,*args,**kwargs):
    print(a,b)
    print(type(args),type(kwargs))
    for x in args:
        print x
    for x in kwargs:
        print(x,kwargs[x])


def main():
    VariableArgsDictionary(10,20,1,2,3,5,7,name="Rashmi",hobby="Teaching")

if __name__ == '__main__':
    main()

'''>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Funtions/cw_3feb/var_arg_dict_eg.py 
(10, 20)
(<type 'tuple'>, <type 'dict'>)
1
2
3
5
7
('hobby', 'Teaching')
('name', 'Rashmi')
>>> '''
