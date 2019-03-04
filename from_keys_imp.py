#WAP to implement your own from keys


def from_keys(input_dict,values=None):
    res=dict()
    keys=input_dict.keys()
    if type(values) == list:
        i=0
        for key in keys:
            if i < len(values):
                res[key]=values[i]
                i += 1
                continue
            res[key] = None
    else:
        res = dict.fromkeys(input_dict,values)
    return res

def main():
    d1={1:1,2:2,3:3}
    #v1=['a','b']
    #v1=['a','b','c','d']
    v1=10
    d2=from_keys(d1,v1)
    
    print d2

if __name__ == '__main__':
    main()

'''
>>> 
== RESTART: C:/Users/Admin/Desktop/Python_2019/Dictionary/from_keys_imp.py ==
{1: 'a', 2: 'b', 3: None}
>>>
'''
'''
>>> 
 RESTART: C:\Users\Admin\Desktop\Python_2019\Dictionary\cw_2_3\from_keys_imp.py 
{1: 'a', 2: 'b', 3: 'c'}
>>>
'''
'''
>>> 
 RESTART: C:\Users\Admin\Desktop\Python_2019\Dictionary\cw_2_3\from_keys_imp.py 
{1: 10, 2: 10, 3: 10}
>>>
'''
