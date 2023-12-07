
math_operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
num_1 = int(input('Enter your first number: '))
num_2 = int(input('Enter your second number: '))

# Addition
print('{} + {} = '.format(num_1, num_2))
print(num_1 + num_1)

# Subtraction
print('{} - {} = '.format(num_1, num_2))
print(num_1 - num_2)

# Multiplication
print('{} * {} = '.format(num_1, num_2))
print(num_1 * num_2)

# Division
print('{} / {} = '.format(num_1, num_2))
print(num_1 / num_2)