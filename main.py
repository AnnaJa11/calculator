
import logging
logging.basicConfig(level=logging.DEBUG)

# Add 2 numbers
def add(num_1,num_2):
    return(num_1 + num_2)
# Subtract 2 numbers
def subtract(num_1,num_2):
    return(num_1 - num_2)
# Multiply 2 numbers
def multiply(num_1,num_2):
    return(num_1 * num_2)
# Divide 2 numbers
def divide(num_1,num_2):
    return(num_1 / num_2)

def prompt_input():
    num_1 = float(input('Enter your first number: '))
    num_2 = float(input('Enter your second number: '))
    
    select = int(input('''
        Please select operation:
        1 for addition
        2 for subtraction
        3 for multiplication
        4 for division
        '''))
    return(num_1,num_2,select)

continue_calculating = True
while continue_calculating is True:
    num_1, num_2, select = prompt_input()
    
    if select == 1:
        logging.info('Dodaje {} i {}. Wynik to '.format(num_1, num_2))
        print(num_1 + num_2)

    elif select == 2:
            logging.info('{} - {} = '.format(num_1, num_2))
            print(num_1 - num_2)

    elif select == 3:
            logging.info('{} * {} = '.format(num_1, num_2))
            print(num_1 * num_2)

    elif select == 4:
        try:
            logging.info('{} / {} = '.format(num_1, num_2))
            print(num_1 / num_2)
        except:
            print("Divsion by 0 not possible!")
    else:
            logging.warning('Invalid operator')

    want_continue = input('Continue? y/n: ').lower()
    if want_continue == "n":
        logging.info('Closing program...')
        continue_calculating = False