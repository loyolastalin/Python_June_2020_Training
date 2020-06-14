'''
Receive input from the user and say hello to him
'''

def printMe(str = "venllia"):
    "Receives the input from the user and say hello to him"
    print("hello user {}".format(str))

def displayEmploeeDetails(name, age, *address):
    "Responsible for printing the employee details"
    # defestive, to check the name is string explicitly
    if(type(name) != type('dummy')):
        print('Name must be string, but you have given {}, please enter the correct input for Name'.format(type(name)))
        return
    print("name : {} age : {}".format(name, age))
    for var in address:
        print(var)
        if(var == 'stalin'):
            return
    print('last statment of the address')
    return

def addingNumbers(*args):
    sum = 0
    for var in args:
        sum = sum + var
    return sum

def main():
    sum = addingNumbers(1,3)
    print(sum)

main()