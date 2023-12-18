#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            division_result = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            division_result = 0
        except (ZeroDivisionError, TypeError):
            if type(my_list_1[i]) not in (int, float) or type(my_list_2[i]) not in (int, float):
                print("wrong type")
            elif my_list_2[i] == 0:
                print("division by 0")
            division_result = 0
        finally:
            result_list.append(division_result)

    return result_list
