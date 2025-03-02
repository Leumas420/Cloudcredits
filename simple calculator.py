def addition (num1, num2):
    result = num1 + num2
    print("Addition : ", result)

def subtraction (num1, num2):
    result = num1 - num2
    print("Addition : ", result)

def multiplication (num1, num2):
    result  = num1 * num2
    print("Addition : ", result)

def division (num1, num2):
    result = round((num1 / num2),2)
    print("Division : ", result)
    
while True:
    
    print("* * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("---------------- SIMPLE CALCULATOR ---------------")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * ")

    print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Quit")
    choice = int(input("Which operation do you want to perform : "))

    a = int(input("Enter first number "))
    b = int(input("Enter second number "))

    if choice == 1:
        addition(a, b)
    elif choice == 2:
        subtraction(a, b)
    elif choice == 3:
        multiplication(a, b)
    elif choice == 4:
        division(a, b)
    elif choice == 5:
        break

    print("* * * * * * * * * * * * * * * * * * * * * * * * * \n\n")

