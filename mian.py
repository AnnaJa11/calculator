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
