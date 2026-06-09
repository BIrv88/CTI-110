# David Irvin
# 06/09/2026
# P1HW!
# A program that solves a math problem that includes adding and subtracting from a starting number.

print("-----Calculating Exponents----")
print()

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
print()

result = base ** exponent 
print(base, "raised to the power of", exponent, "is", result, "!!")
print()

print("-----Addition and Subtraction----")
print()
num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter an integer to add: "))
num3 = int(input("Enter an integer to subtract: "))
print()

sum_result = num1 + num2
final_result = sum_result - num3 

print(num1, "+", num2, "-", num3, "is equal to", final_result)
