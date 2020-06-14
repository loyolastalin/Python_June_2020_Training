num1 = 10
num2 =10

def getInput(a):
    "Input from the method.. what ever you put in it will be diplayed"
    global num1, num2
    num1 = 20
    num2 =  20

def main():
    getInput(23)
    print(num1)
    print(num2)

if __name__ == "__main__":
    main()
