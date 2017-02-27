"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

"""
# PART 1a

#(a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

home_town = "Westfield"
first_name = "Erika"
last_name = "Kettleson"

def my_town_name(home_town):
    """ tests if parameter (strings) match my hometown
    """
    if home_town.lower() == "westfield":
        # catch upper case entries
        return True
    else:
        return False 

my_town_name(home_town)

# PART 1b

# (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.


def concatenate_name(first_name, last_name):
    """ concatenate two strings and return a single string
    """
    full_name = (first_name + " " + last_name)
    # adding whitespace between names
    return full_name


concatenate_name(first_name, last_name)

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.

def getting_to_know_you(home_town, first_name, last_name):
    """ greets user with name and message based on results of name & home town fxns
    """
    if my_town_name(home_town) == True:
        print "Hi {} Wow we're from the same place! CRAZY!".format(concatenate_name(first_name, last_name))
    else:
        print "Well, {}, where are you from?".format(concatenate_name(first_name, last_name))


getting_to_know_you(home_town, first_name, last_name)



"""

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

PART THREE: Write your own function declarations - Part 3 questions aren't
included in the doctest.

"""

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.



###############################################################################

# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."


def is_berry(fruit):
    """Determines if fruit is a berry"""
    approved_fruits = ("strawberry", "cherry", "blackberry")
    # list of 3 fruits to check against
    if fruit in approved_fruits:
        return True
    else:
        return False
is_berry("cherhhhhhry")


# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.

def shipping_cost(fruit):
    """Calculates shipping cost of fruit"""
    if is_berry(fruit):
        # checking truthiness of is_berry and printing message 
        return 0
    elif is_berry(fruit) == False:
        return 5

shipping_cost("cherhhhhzzzry")


# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.

def append_to_list(lst, num):
    """Creates a new list consisting of the old list with the given number
       added to the end."""
    new_list = []
    # new list concatenating list and num
    for item in lst:
        if len(new_list) < len(lst):
            # iterate throgh whole lst and append to new list
            new_list.append(item)
            continue
    new_list.append(num)
    # outside for loop - after all items in lst are appended - add num
    print new_list

append_to_list([1, 2, 3], 4)

# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.

def calculate_price(base_item_price, state, tax):
    # function taking a price, state & tax and returning state specific totals

    pre_fee_price = (base_item_price + (base_item_price * tax))
    # total for all states besides fee-states
    pa_total_price = pre_fee_price + 2
    # pa specific price
    ma_total_low_price = pre_fee_price + 1
    # ma specific price for items under 100 dollars
    ma_total_high_price = pre_fee_price + 3
    # ma specific price for items over 100 dollars
    ca_total_price = (pre_fee_price + (pre_fee_price * .03))
    # ca specific price
    tax = .05
    state = state.lower()
    # ensuring state variables are consistent

    if state == 'ca':
        total_price = ca_total_price
        return total_price
    elif state == 'pa':
        total_price = pa_total_price
        return total_price
    elif state == 'ma':
        if base_item_price <= 100:
            total_price = ma_total_low_price
            return total_price
        else:
            total_price = ma_total_high_price
            return total_price
    else:
        total_price = pre_fee_price
        return total_price


calculate_price(100, 'ma', .05)



# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.


def list_append(lst, *args):
    # fxn takes a list and *args to allow any number of extra arguments
    return lst + [arg for arg in args]
    # return the original list (lst) and list comphrehension through all args

list_append([1, 2, 3], 45, 4, 67)

# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

def nested_word_function(n):
    # function to triple word with function nested inside
    def triple_word(word):
        # return word ** n 
        return word + word + word
    return triple_word(n)

print nested_word_function("drew")


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.


# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.



if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
