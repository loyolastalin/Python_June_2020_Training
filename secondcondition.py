'''
  Get the user wages and find the happiness
'''

try:
    getSalary = int(input('Enter the week wages'))

    if(getSalary >= 80):
        print("I\'m happy")
    else:
        print('Sad!!!')
except:
    print('error')

print('Program successfully completed...')