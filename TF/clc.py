operator = input(f"operator [/, *, +, -]: ")
firstNumber = int(input(f"first number: "))
secondNumber = int(input(f"second number: "))

if operator == '/':
    print(firstNumber / secondNumber)
elif operator == '*':
    print(firstNumber * secondNumber)
elif operator == '+':
    print(firstNumber + secondNumber)
elif operator == '-':
    print(firstNumber - secondNumber)
else:
    print(f"invalid operator")