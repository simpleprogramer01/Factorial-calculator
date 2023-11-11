#simple programmer
# A script to calculate the factorial of numbers

num1 = 0
while True:
    # Receive numbers and control tasks and errors :
    try:
        num1 = int(input("Enter the integer numbers : "))
        if num1<0:
            raise RuntimeError('Negative is not allowed ')
    except ValueError as ERR:
        print('enter a valid number ',ERR)
    except RuntimeError as ERR:
        print(ERR)
    else:
        break
#Calculate the factorial of a number and print :
FACT = 1
while num1!=0 and num1!=1:
    FACT*= num1
    num1 -=1
print(f'factorial = {FACT}')
