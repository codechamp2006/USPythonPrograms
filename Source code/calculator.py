while True:
    num1 = int(input("Enter 1st number:"))
    num2 = int(input("Enter 2nd number:"))
    eq = input()
    if eq == "Stop":
        break
    elif eq == "+":
        print(num1+num2)
    elif eq == "-":
        print(num1-num2)
    elif eq == "/":
        print(num1/num2)
    elif eq == "*":
        print(num1*num2)
