#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Replaces all occurances of an element by another in new list
    new_list = []

    for item in my_list:
        # Check if the current element is the one to replace
        if item == search:
            # Append the replace value if it matches
            new_list.append(replace)
        else:
                # Otherwise, a append the original element
                new_list.append(item)

        # Return the new list with replacements
        return new_list
