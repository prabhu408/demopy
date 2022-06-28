a=5
b=2

try:
    print(a/b)
    k=int(input("Enter a number"))
    print(k)
except ZeroDivisionError as e:
    print("Division by zero error", e)
except ValueError as e:
    print("Invalid input", e)
except Exception as e:
    print("something went wrong....", e)