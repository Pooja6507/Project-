print("Select an operation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("5. square")
print("6. square root")

operation = input()

if operation == "1":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The difference is " + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The product is " + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The result is " + str(int(num1) / int(num2)))
elif operation == "5":
    num1 = input("Enter first number: ")
    print("The result is " + str(int(num1) * int(num1)))
elif operation == "6":
    import math
    num1 = int(input("Enter first number: "))
#   use mat module
#   num1_sqrt = num1 ** 0.5
    num1_sqrt = math.sqrt(num1)
    print("The result is " + str((num1, num1_sqrt)))

else:
    print("Invalid Entry")
