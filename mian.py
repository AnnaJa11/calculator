def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

select = {
  "1": add,
  "2": subtract,
  "3": multiply,
  "4": divide,
}


def calculator():
    num1 = float(input("What's the first number?: "))
    for operation in select:
        print(operation)
    should_continue = True

    while should_continue:
        user_operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        user_calculation = select[user_operation]
        answer = user_calculation(num1, num2)
        print(f"{num1} {user_operation} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            print("Goodbye! ")

            calculator()

          
calculator()
  