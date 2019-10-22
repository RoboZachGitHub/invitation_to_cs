# Schneider & Gersting
# Invitation to CS
# Ch. 2
# challenge work Problem 2
# implementation of selection sort

from big_bigger_biggest import largest_value_w_position


def selection_sort(unsorted_list: list):
    #print(unsorted_list)
    sorted_list = []
    while len(unsorted_list) > 0:
        value, i_position = largest_value_w_position(unsorted_list)
        unsorted_list.pop(i_position)
        sorted_list.insert(0, value)
    #print(sorted_list)
    return sorted_list


numbers_list = [19, 41, 12, 63, 22]

selection_sort(numbers_list)
