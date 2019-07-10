"""
File: khansole_academy.py
---------------------------
This program is the capstone educational software product of your
shirt time in CS106AP so far! For more details, see the Assignment 2
handout.
"""

import random

TOTAL_PROBLEMS = 5
MIN_THRESHOLD = 0
MAX_THRESHOLD = 30


def user_prompt():
    """
    This function returns the prompt that the user is presented with to choose
    what kind of problem they want to practice.
    """
    return """
    Enter the number of the type of arithmetic problem you want to practice.
    1) Addition
    2) Subtraction
    """


def generate_input():
    """
    This function generates a random number to act as input for an
    arithmetic problem. For more documentation on the Python random module, go
    to this link: https://docs.python.org/3.7/library/random.html
    """
    return random.randint(MIN_THRESHOLD, MAX_THRESHOLD)


def create_arithmetic_problem_prompt(a, b, operator):
    """
    This function takes in two numbers and an operator and returns a string
    that is built from these three pieces of information
    """
    return "What is " + str(a) + " " + operator + " " + str(b) + "?"


def assess_user_response(user_answer, true_answer):
    """
    This function takes in two answers, one of which is provided by
    the user and one of which is the correct answer. It generates an
    appropriate response depending on whether or not the user answers
    matches the correct answer.
    """
    if user_answer == true_answer:
        print("Correct, great work!")
        return True
    else:
        print("Incorrect. The expected answer was " + str(true_answer))
        return False


def addition(a, b):
    """
    Simple function to encapsulate addition
    """
    return a + b


def subtraction(a, b):
    """
    Simple function to encapsulate subtraction
    """
    return a - b


def main():
    """
    This console program currently implements some of the basic functionality
    of Khansole Academy. It currently only supports two problem types (addition
    and subtraction) and keeps track of how many problems the user gets correct.
    """
    num_problems_done = 0
    num_correct = 0
    while num_problems_done < TOTAL_PROBLEMS:
        print(user_prompt())
        choice = int(input("Your choice: "))
        a = generate_input()
        b = generate_input()
        if choice == 1:
            print(create_arithmetic_problem_prompt(a, b, "+"))
            user_answer = int(input("Your answer: "))
            true_answer = addition(a, b)
            correct = assess_user_response(user_answer, true_answer)
            if correct:
                num_correct += 1
            num_problems_done += 1
        elif choice == 2:
            print(create_arithmetic_problem_prompt(a, b, "-"))
            user_answer = int(input("Your answer: "))
            true_answer = subtraction(a, b)
            correct = assess_user_response(user_answer, true_answer)
            if correct:
                num_correct += 1
            num_problems_done += 1
        else:
            print("Sorry, you didn't choose a valid option!")
    print("You got " + str(num_correct) + " problems correct!")


if __name__ == "__main__":
    main()
