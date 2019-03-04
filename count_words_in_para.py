#WAP to accept a paragraph from user and return a dict of count of words


def DictWords(p):
    res=dict()

    for ch in p.split():
        if res.get(ch) != None:
            res[ch] += 1
        else:
            res[ch] = 1
    
    return res

def main():
    p1=input('Enter a paragraph:')
    d1=DictWords(p1)
    print d1

if __name__ == '__main__':
    main()

'''
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Dictionary/count_words_in_para.py 
Enter a paragraph:'Hi hello how are you hello all of you'
{'all': 1, 'of': 1, 'how': 1, 'Hi': 1, 'are': 1, 'you': 2, 'hello': 2}
>>> 
'''
