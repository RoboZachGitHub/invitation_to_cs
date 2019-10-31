# Schneider & Gersting
# Invitation to CS
# searching/matching algorithms from Ch. 3
# Ch. 3: the efficiency of algorithms


def binary_search(sorted_list: list, number: int):
    """ searches a sorted list of integers for the given integer using the standard binary search algorithm """

    found = False
    i_beginning = 0
    i_end = len(sorted_list) - 1
    while not found and i_beginning <= i_end:
        i_middle = int((i_end + i_beginning)/2)
        num_mid = sorted_list[i_middle]
        if number == num_mid:
            found = True
        elif number < num_mid:
            i_end = i_middle - 1
        else:
            i_beginning = i_middle + 1
    return found


# test_list = [1,2,3,4,5,7,8,9]
# t_or_f = binary_search(test_list, 6)
# print(t_or_f)
