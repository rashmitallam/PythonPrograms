#WAP to accept a filename from user and print those lines who have less than or equal to 80 characters
#Also print line numbers which have more than 80 characters, stating than line is having more than standard count of characters


def PrintFileLineLessThan80Chars(file):
    fd=open(file)
    if fd != None:
        line=fd.readline()
        line_no=0
        line_numbers=[]
        while line != '':
            line_no += 1
            if len(line) <= 80:
                print line
            else:
                line_numbers.append(line_no)
                #print 'Line number '+str(line_no)+' has more that 80 chars!\n'
            line=fd.readline()
    print("Line numbers of lines having more than 80 chars are:",line_numbers)


def main():
    f=input('Enter filename to be printed:')
    PrintFileLineLessThan80Chars(f)




if __name__ == '__main__':
    main()

'''
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/File_handling/cw_3_3/print_lines_80_chars.py 
Enter filename to be printed:'test.txt'
alskklk

ascacacacace

swqdwacjnjknbjbjojojosw

sadsad

Line number 5 has more that 80 chars!

ackjjnjbjkbqwjk kma

adhbhkbwjb cf,

wdbjjkwbdjkbwq,dawhcbdwjabcjq.

wadcbjwqbjkwqbfkjfb qwjcf

Line number 10 has more that 80 chars!

>>> 
'''
'''
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/File_handling/cw_3_3/print_lines_80_chars.py 
Enter filename to be printed:'test.txt'
alskklk

ascacacacace

swqdwacjnjknbjbjojojosw

sadsad

ackjjnjbjkbqwjk kma

adhbhkbwjb cf,

wdbjjkwbdjkbwq,dawhcbdwjabcjq.

wadcbjwqbjkwqbfkjfb qwjcf

('Line numbers of lines having more than 80 chars are:', [5, 10])
>>> 
'''
