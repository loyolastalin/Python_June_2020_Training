# To Find out given number is prime or not
# input

def displayPaysilp(employeeName, basicPay):
    if (basicPay <= 3500):
        hra = 5/100 * basicPay 
    elif (basicPay <= 10000) :
        hra = 10/100 * basicPay     
    else:
        hra =  12/100 * basicPay

    hra = 12/100 * basicPay 
    pf = 5/100 * basicPay
    crossSalary = basicPay + hra + hra
    deduction = pf + 200
    betSalary = crossSalary - deduction
    astri = "*" * 100
    print("\tEmployee Salary\n {}\n * Name\t\t:{}\t\tBasic Pay\t:{}\n * HRA\t\t: {}\n {}".format(astri, employeeName, basicPay, hra, astri))

def main():
    employeeName = input ("Enter the Employee Name: ")
    basicPay = float(input("Enter the Basic Pay: "))
    displayPaysilp(employeeName, basicPay)

main()