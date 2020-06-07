'''
 Get the value from user and print the number is even or odd
x % 2 == 0
a = x% 2
a==0
'''
# input
getNumber = int(input("Enter the numnber :"))
# process
reminder = getNumber % 2

if(reminder == 0):
    print('Event number')
else:
    print('odd number')



# out
