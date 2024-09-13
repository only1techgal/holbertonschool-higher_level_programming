#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    # Divides elements by element 2 lists
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")

            elem1 = my_list_1[i]
            elem2 = my_list_2[i]

            if not (isinstance(elem1, (int, float)) and
                    isinstance(elem2, (int, float))):
                raise TypeError("wrong type")

            result.append(elem1 / elem2)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass

    return result
