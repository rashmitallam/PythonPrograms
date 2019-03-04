#WAP to accept a filenme from user and print the smallest and the longest line from it

def PrintSmallestLongestLineInFile(file):
    fd=open(file)
    line=fd.readline()
    min_line=line
    max_line=line
    while line != '':
        line=fd.readline()
        if line == '\n' or line == '':
            continue
        if len(line)<len(min_line):
            min_line=line
        elif len(line)>len(max_line):
            max_line=line
    return min_line,max_line

    
def main():
    f=input('Enter the filename to be printed:')
    min,max=PrintSmallestLongestLineInFile(f)
    print('\nSmallest Line = {0}\nLongest Line = {1}'.format(min,max))


if __name__ == '__main__':
    main()

'''
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/File_handling/cw_3_3/print_smallest_longest_line_in_file.py 
Enter the filename to be printed:'test1.txt'

Smallest Line = rgg

Longest Line = wefjkrnfekjfjjefjlnfklejnrfklenrefreg

>>> 
'''
