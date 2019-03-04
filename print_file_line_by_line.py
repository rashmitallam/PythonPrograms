#WAP to accept a filename from user and print it line by line



def PrintFileLineByLine(file):
    fd=open(file)
    if fd != None:   #Check if file exists
        line = fd.readline()
        while line != '':
            print line
            line = fd.readline()

def main():
    f=input("Enter filename to be printed:")
    PrintFileLineByLine(f)


if __name__ == '__main__':
    main()

'''
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/File_handling/cw_3_3/print_file_line_by_line.py 
Enter filename to be printed:'test.txt'
alskklk

ascacacacace

swqdwacjnjknbjbjojojosw

sadsad

ackjjnjbjkbqwjk kma

adhbhkbwjb cf,

wdbjjkwbdjkbwq,dawhcbdwjabcjq.

wadcbjwqbjkwqbfkjfb qwjcf

>>> 
'''
