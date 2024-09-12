#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Replaces all occurances of an element by another in new list
    new_list = [replace if item == search else item for item in my_list]
    return new_list    
    
if __name__ == "__main__":
    # Define the lists and replacements to be tests
    test_cases = [
        ([1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89], 2, 89),
        ([1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89], 4, 2)
    ]

    for my_list, search, replace in test_cases:
        result = search_replace(my_list, search, replace)
        print(result)  # Print each result on a new line
