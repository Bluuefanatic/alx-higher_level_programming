#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the replaced values
    new_list = []

    # Iterate through the elements of the input list
    for element in my_list:
        # Replace the element if it matches the search criteria
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)

    return new_list
