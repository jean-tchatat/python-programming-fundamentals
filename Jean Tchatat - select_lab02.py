# Filename: select_lab02.py
# Name: Jean Tchatat
# COSC 175 HWK05

# 11
print(f"#11. Two integer calculations")
first_integer = int(input("Enter the first integer: "))
second_integer = int(input("Enter the second integer: "))
sum_result = first_integer + second_integer
difference_result = first_integer - second_integer
product_result = first_integer * second_integer
print(f"Inputs: first integer={first_integer}, second integer={second_integer}")
print(f"Sum={sum_result}")
print(f"Difference={difference_result}")
print(f"Product={product_result}")
if second_integer != 0:
    quotient_result = first_integer / second_integer
    print(f"Quotient={quotient_result}\n")
else:
    print(f"Quotient cannot be calculated: division by zero.\n")

# 12
print(f"#12. Calculator menu")
print(f"1. Sum")
print(f"2. Difference")
print(f"3. Product")
print(f"4. Quotient")
choice = int(input("Enter an integer choice: "))
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
if choice == 1:
    result = first_number + second_number
elif choice == 2:
    result = first_number - second_number
elif choice == 3:
    result = first_number * second_number
elif choice == 4:
    if second_number != 0:
        result = first_number / second_number
    else:
        result = "Error: division by zero."
else:
    result = "Error: choice must be 1, 2, 3, or 4."
print(f"Code={choice}, first number={first_number}, second number={second_number}")
print(f"Result={result}")
