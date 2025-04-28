import math
running = True

calcs = input("Normal, quadratic or scientific calculator (q/n/s)?:  ")

if calcs == "n":

    while running:
        operator = input("Enter an operator (/ + - * ^ surd):  ")
        
        num1 = float(input("Enter your first number:  "))
        num2 = float(input("Enter the second number:  "))
        p = "product"
        e = "exponent"
        s = "subtraction"
        a = "addition"
        d = "division"

        if operator == "+":
            result = num1 + num2
            print(f"{result:.2f}")
        elif operator == "-":
            result = num1 - num2
            print(f"{result:.2f}")
        elif operator == "/":
            result = num1 / num2
            print(f"{result:.2f}")
        elif operator == "*":
            result = num1 * num2
            print(f"{result:.2f}")
        elif operator == "^":
            result = pow(num1, num2)
            print(f"{result:.2f}")
        elif operator == "surd":
             result = num1 * (math.sqrt(num2))
             print(f"{result:.2f}") 
        else:
            print(f"{operator} is not valid operator")
            
        cont_calc = input("Continue calculating (y/n)?:  ").lower()
        if cont_calc == "y":
                running = True
        elif cont_calc == "n":
                running = False

elif calcs == "s":
     
    while running:
        operator = input("Enter an operator (% sin cos tan sinh cosh tanh sqrt log pi):  ")
        
        num = float(input("Enter the number:  "))

        if operator == "sin":
            result = math.sin(num)
            print(f"{result:.4f}")
        elif operator == "cos":
            result = math.cos(num)
            print(f"{result:.4f}")
        elif operator == "tan":
            result = math.tan(num)
            print(f"{result:.4f}")
        elif operator == "sinh":
            result = math.sinh(num)
            print(f"{result:.4f}")
        elif operator == "cosh":
            result = math.cosh(num)
            print(f"{result:.4f}") 
        elif operator == "tanh":
            result = math.tanh(num)
            print(f"{result:.4f}")
        elif operator == "sqrt":
            result = math.sqrt(num)
            print(f"{result:.2f}")
        elif operator == "log":
            result = math.log(num)
            print(f"{result:.4f}")
        elif operator == "pi":
             print(math.pi)
        else:
            print(f"{operator} is not valid operator")
            
    cont_calc = input("Continue calculating (y/n)?:  ").lower()
    if cont_calc == "y":
            running = True
    elif cont_calc == "n":
            running = False
    else:
        print("Enter valid response")

elif calcs == "q":
    a = float(input("Enter coefficient A:  "))
    b = float(input("Enter coefficient B:  "))
    c = float(input("Enter coefficient C:  "))

    d = b**2 - 4*a*c
    if d < 0:
        print("No real roots")
    elif d == 0:
         -b / (2*a)
    else:
        root1 = (-b + math.sqrt(d) / 2*a)
        root2 = (-b - math.sqrt(d) / 2*a)
        print(f"Roots are: {root1} and {root2}")
# Made by ~tobi_adabs