#WAP to accept an integer from user and print its table

num=input("Enter the number whose table is to be printed:")

#range(start_index,end_index,step_value)- end_index is excluded

for x in range(1,11):
    y=num*x
    print(str(num)+'*'+str(x)+'='+str(y))

'''Output
Enter the number whose table is to be printed:2
2*1=2
2*2=4
2*3=6
2*4=8
2*5=10
2*6=12
2*7=14
2*8=16
2*9=18
2*10=20
'''

#HW
#WAP to accept n an integer from user and print tables from 2 to n - done
