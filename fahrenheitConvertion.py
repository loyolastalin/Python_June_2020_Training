# fahrenheit conversion

def fahrenheitToCelicus(a):
    convertion = (a - 32) * 5/9 
    return convertion

def main():
    inputValue = 100
    result = fahrenheitToCelicus(inputValue)
    print("Fahrenheit for {} is {:.2f}".format(inputValue, result))

main()

