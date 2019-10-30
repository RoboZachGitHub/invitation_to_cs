# Schneider & Gersting
# Invitation to CS
# sorting algorithm(s) from Ch. 3
# Ch. 3: the efficiency of algorithms

# ch_2 directory must be in the python configuration
from big_bigger_biggest import largest_value_w_position_2


def swap_list_positions(list_to_mod, pos_a, pos_b):
    """ swaps the positions of two list items and returns the modded list"""
    list_to_mod[pos_a], list_to_mod[pos_b] = list_to_mod[pos_b], list_to_mod[pos_a]
    return list_to_mod


def selection_sort(integers_list: list):
    """ a basic selection sorting algorithm. a different version was implemented as a ch 2 challenge problem"""

    tmp_list = integers_list
    i = len(tmp_list) - 1  # set index to end of list
    while i > 0:
        value, pos = largest_value_w_position_2(tmp_list[:i+1])
        swap_list_positions(tmp_list, pos, i)
        i -= 1
    sorted_list = tmp_list
    return sorted_list


# test_list = [1, 5, 7, 2, 8, 3, 22, 78, 0]

# print(test_list)
# sorted_test_list = selection_sort(test_list)
# print(sorted_test_list)
