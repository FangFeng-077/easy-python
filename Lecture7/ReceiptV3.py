# Constants
TAX = 0.0725
PEOPLE_THRESHOLD = 5
LARGE_PARTY_TIP = 0.20
SMALL_PARTY_TIP = 0.15


def get_tip(total_cost, num_people):
    """
    Returns the tip given the `total_cost` of a meal
    and the number of people who ate. Larger parties
    pay a larger tip.
    """
    if num_people > PEOPLE_THRESHOLD:
        return total_cost * LARGE_PARTY_TIP
    else:
        return total_cost * SMALL_PARTY_TIP


def get_tax(total_cost):
    """
    Returns tax given the `total_cost` of a meal
    """
    return total_cost * TAX


def calculate_total(total_cost, num_people):
    """
    Given the total_cost of a meal and the number of
    people who ate, returns the total for the meal
    including tax and tip.
    """
    tip = get_tip(total_cost, num_people)
    tax = get_tax(total_cost)
    return total_cost + tip + tax


def calculate_meal_total():
    """
    This program calculates how much a meal costs including
    tax and tip. The tip is based on the number of people in
    the party and the original amount of the bill, both of which
    are inputted by the user. The program continues to prompt the
    user until the user enters -1 as a means of exiting the program.
    """
    print('This program calculates the total bill amount for a meal at Treehouse.')
    num_people = int(input('Enter the number of people in your party (or -1 to quit) : '))
    while num_people != -1:
        total_cost = float(input('Enter the cost of your bill before tax and tip: '))
        final_cost = calculate_total(total_cost, num_people)
        print('The final cost of your meal is ' + str(final_cost))
        num_people = int(input('Enter the number of people in your party (or -1 to quit) : '))
    print('Goodbye!')


if __name__ == '__main__':
    calculate_meal_total()