# simple calculator

print("Select an operation to perform")

print("1 ADD")
print("2 SUBTRACT")
print("3 MULTIPLY")
print("4 DIVIDE")
print("5 QUIT")

calculator_operation = ['add', 'subtract', 'divided', 'multiply']


while True:
    operation = int(input())

    if operation == 5:
        break

    
    if operation not in range(0,5):
        print("You have entered an invalid choice") 

    else:
        num1 = int(input("please enter the first number: "))
        num2 = int(input("Please enter the second number: "))

        if operation == 1:
            sum = num1 + num2
            print(f"The sum of {num1} and {num2}: {sum}")

        elif operation == 2:
            difference = num1 - num2
            print(f"The difference of {num1} and {num2}: {difference}")

        elif operation == 4:
            product = num1 * num2
            print(f"The quotient of {num1} and {num2}: {product}")

        elif operation == 3:
            if num1 != 0:
                quotient = num1 / num2
                print(f"The quotient of {num1} and {num2}: {quotient}")
            else:
                print("You can not divided by zero")


       