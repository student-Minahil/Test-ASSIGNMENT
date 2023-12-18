# program 1
num1 = int (input ("enter a number"))
num2 = int (input("enter a number"))
if num1 % 2==1 and num2 % 2==1:
    result=(num1*num1)+(num2*num2)
    print(result)
else:
    print ("calculation is not performed")

# program 2
def calculate_factorial(number):
    if number < 0:
        print("factorial is not defined for negative number.")
        return None
    factorial_result = 1
    while number > 1:
        factorial_result *=number
        number -= 1
    return factorial_result
user_input = int(input("enter a number to calculate its factorial: "))
result = calculate_factorial(user_input)
if result is not None:
    print(f"the factorial of {user_input} is: {result}")

# program 3
import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    max_attempts = 5
    print("welcome to the guess the number game!")
    print("i have selected a number between 1 and 100. try to guess it!")
    for attempt in range(1, max_attempts + 1):
        user_guess = int(input("attempt {}: enter your guess: ".format(attempt)))
        if user_guess < secret_number:
            print("too low! try again.")
        elif user_guess > secret_number:
            print("too high! try again.")
        else:
            print("congratulation! you guessted the number.")
            return
    print("game over! you run out of guesses.")
    print("the correct number was {}.".format(secret_number))

    # program number 4
    def resturant_bill_calculator():
        num_people = int(input("enter the number of people:"))
        cost_per_meal = float(input("enter the cost of each meal: $"))
        sales_tax_percentage = float(input("enter the tips percentage:"))
        tips_percentage = float(input("enter the tips percentage: "))
        total_cost_of_food = num_people * cost_per_meal
        total_sales_tax = total_cost_of_food * (sales_tax_percentage / 100)
        total_tip_amount = total_cost_of_food * (tips_percentage / 100)
        total_bill_amount = total_cost_of_food + total_sales_tax + total_tip_amount
        bill_amount_per_person = total_bill_amount / num_people
        print("\nbill summary:")
        print("total cost of food: ${:.2f}".format(total_cost_of_food))
        print("total sales tax: ${:.2f})".format(total_sales_tax))
        print("total tip amount: ${:.2f})".format(total_tip_amount))
        print("total bill amount: ${:.2f})".format(total_bill_amount))
        print("bill amount per person: ${:.2f})".format(bill_amount_per_person))