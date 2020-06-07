age =  int(input('Age ?: '))

# one way
if(age < 10):
    print('one way age < 10')

if(age<20):
    print('one way < 20')


# multi way
if(age < 10):
    print(' multi way age < 10')
elif(age<20):
    print(' multi way between 10 and 20')
else:
    print('age > 20')