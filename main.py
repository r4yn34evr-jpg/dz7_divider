print("Welcome to the GREAT DIVIDER", "\nNow enter a couple of numbers")

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    div = num1 / num2

except ZeroDivisionError:
    print('You can\'t divide by zero')
except ValueError:
    print("Value Error")

else:
    print("Result is", round(div, 2))

finally:
    print("Hasta la vista!")