
def A(x, y):
    return x + y

def S(x, y):
    return x - y

def M(x, y):
    return x * y

def D(x, y):
    return x / y


print("Select operation.")
print("1.A")
print("2.S")
print("3.M")
print("4.D")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", A(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", S(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", M(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", D(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")