# To Find out given number is prime or not
# input
givenNumber=int(input("Enter the number:"))

def prime(numer):
    if(givenNumber == 1):
        print("{} is not prime".format(givenNumber))  
        return  
    elif givenNumber == 2:
        print("{} is prime".format(givenNumber))
        return
    else:
        for i in range (2, givenNumber):
            if(givenNumber % i == 0):
                print('not prime')

    print('prime')

