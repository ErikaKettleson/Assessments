"""List Assessment 

Edit the functions until all of the doctests pass when
you run this file.
"""


def all_odd(numbers):
    """Return a list of only the odd numbers in the input list.

    For example::

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """
    odd_list = [number for number in numbers if number % 2 != 0]
    return odd_list


all_odd([1, 2, 3, 4, 5])


def print_indices(items):
    """Print index of each item in list, followed by item itself.

    Do this without using a "counting variable" --- that is, don't
    do something like this::

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this::

        >>> print_indices(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

        >>> print_indices(["Toyota", "Jeep", "Toyota", "Volvo"])
        0 Toyota
        1 Jeep
        2 Toyota
        3 Volvo

    """
    for index in range(0, len(items)):
        print index, items[index]

print_indices(["Toyota", "Jeep", "Volvo"])


def foods_in_common(foods1, foods2):
    """Find foods in common.

    Given 2 lists of foods, return the items that are in common
    between the two, sorted alphabetically.

    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists). Is there another that would be a good idea?

    For example::

        >>> foods_in_common(
        ...     ["cheese", "bagel", "cake", "kale", "zebra cakes"],
        ...     ["hummus", "cheese", "beets", "kale", "lentils", "bagel", "cake" ]
        ... )
        ['bagel', 'cake', 'cheese', 'kale']
        
    If there are no foods in common, return an empty list::

        >>> foods_in_common(
        ...     ["lamb", "chili", "cheese"],
        ...     ["cake", "ice cream"]
        ... )
        []

    """
    # my version with sets but not alphabetical :(

    # food_set1 = set(foods1)
    # food_set2 = set(foods2)

    # duplicate_items = set.intersection(food_set1, food_set2)
    # duplicate_items = list(duplicate_items)

    # return duplicate_items

    # another chic-looking attempt that is not sorted alphabetically

    # duplicate_foods = [food for food in foods1 if food in foods2]
    # return duplicate_foods

    #honestly do not know how to sort alphebetically w/o sorted

    duplicate_foods = []

    for food in foods1:
        if food in foods2:
            duplicate_foods.append(food)
    return sorted(duplicate_foods)     

    # while duplicate_foods:
    #     minimum = duplicate_foods[0]
    #     for food in duplicate_foods:
    #         if food < minimum:
    #             minimum = food
    #     sorted_foods.append(minimum)

    return duplicate_foods.sort()     


foods_in_common(["cheese", "bagel", "cake", "kale", "zebra cakes"],
                ["hummus", "cheese", "beets", "kale", "lentils", "bagel", "cake"]
                )


def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example::

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(
       ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
       ... )
       ['you', 'are', 'good', 'at', 'code']
    """
    every_other_list = []

    for item in items:
        every_other_list = items[::2]
        return every_other_list


def largest_n_items(items, n):
    """Return the `n` largest integers in list, in ascending order.

    You can assume that `n` will be less than the length of the list.

    For example::

        >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [59, 700, 6006]

    It should work when `n` is 0::

        >>> largest_n_items([3, 4, 5], 0)
        []

    If there are duplicates in the list, they should be counted
    separately::

        >>> largest_n_items([3, 3, 3, 2, 1], 2)
        [3, 3]
    """

    largest_n_list = []

    for item in items:
        # items[::-1].sort()
        items = sorted(items, reverse=True)
        # items = items[::-1]
        largest_n_list = sorted(items[:n])

    return largest_n_list

largest_n_items([3, 3, 3, 2, 1], 2)  

    # this fxn iterates throgh items, assigns the first number as 
    # maximum and reassigns if higher number comes along


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
