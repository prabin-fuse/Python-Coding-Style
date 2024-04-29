### Exception Handling Assignment day2:
import logging

logging.basicConfig(level=logging.DEBUG, filename="exception_logs.log",
                    format="%(asctime)s:%(levelname)s:%(message)s")


class InvalidAgeError(Exception):
    pass

class WeakPassowrdError(Exception):
    pass


##########functions:
def division(num1, num2):

    try:
        ans = num1/num2
        #print(f"The answer of dividing {num1} by {num2} is : {ans} ")
        logging.info(f"The answer of dividing {num1} by {num2} is : {ans} ")
    except ZeroDivisionError as e:
        logging.warning("Error! Divisor is zero. Please change it or handle it.")
    

def user_file():
    try:    
        file_name = input("\n\nPlease give the file name you want to access : ")
        logging.info(f"\nReading from {file_name} :" )
        file = open(file_name)
        content = file.read()
        logging.info(content)
    except FileNotFoundError:
        logging.error("The required file is not found")


def convert_to_int(str):
    print(f"Original Input : {str}")
    try:
        #print(f"Converted to integer : {int(str)}")
        logging.info(f"Converted to integer : {int(str)}")
    except ValueError:
        logging.error("The given input cannot be converted into integer. Please give integer compatible string.")
    

def division_both_error(num1, num2):
    try:
        ans = num1/num2
        #print(f"The answer of dividing {num1} by {num2} is : {ans} ")
        logging.info(f"The answer of dividing {num1} by {num2} is : {ans} ")
    except ZeroDivisionError as e:
        logging.error("Error! Divisor is zero. Please change it or handle it.")
    except ValueError:
        logging.error("The given value is not interger or float")


def check_user_age():
    age = int(input("Please input your age : "))
    try:
        if age < 0 or age > 120:
            raise InvalidAgeError()
        else: 
            #print("Your age is valid")
            logging.info("Your age is valid")
    except InvalidAgeError as e:
        logging.error("InvalidAge Error!  Your age must be between 0 and 120.")

def check_password():
    password = input("Please provide your password : ")
    try:
        if len(password) < 8:
            raise WeakPassowrdError("WeakPasswordErrorr! Your password is weak. i..e less than 8 characters.")
        else:
            #print("Valid password!")
            logging.info("Valid password!")
    except WeakPassowrdError as e:
        logging.error(f"Error :  {e}")



### testing functions:
def testing_functions():
    print("1) Division => ZeroDivisionError")
    print("2) Filename and read content")
    print("3) Integer conversion")
    print("4) Division => ZeroDivisionError and Value Error")
    print("5) Age validation check")
    print("6) Password strength test")

    option = int(input("\nChoose the options : "))
    #print(option)

    if option == 1:
        num1 = int(input("Enter the dividend : "))
        num2 = int(input("Enter the divisor : "))
        division(num1, num2)
    elif option == 2:
        user_file()
    elif option == 3:
        string = input("Enter the string to type cast in integer : ")
        convert_to_int(string)
    elif option == 4:
        num1 = int(input("Enter the dividend : "))
        num2 = int(input("Enter the divisor : "))
        division_both_error(num1, num2)
    elif option == 5:
        check_user_age()
    elif option == 6:
        check_password()
    else:
        print("Invaliid optionss")




### main

testing_functions()



