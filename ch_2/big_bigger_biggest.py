# Schneider & Gersting
# Invitation to CS
# Ch. 2.3.3

# find largest value in a list
# print its value and its position in the list


def largest_value_w_position(numbers_list: list):
    # same as largest_value_w_position, but using a while loop
    largest = numbers_list[0]
    i_largest = 0
    i = 1
    while i < len(numbers_list):
        value = numbers_list[i]
        if value > largest:
            largest = value
            i_largest = i
            i += 1
        else:
            i += 1

    # print("using largest_value_w_position_2")
    # print("""largest value is: {}\nposition index is: {}\n""".format(largest, i_largest))
    return largest, i_largest

def largest_value_w_position_2(list_of_numbers: list):
    tmp_largest = list_of_numbers[0]
    i_largest = 0
    for i, value in enumerate(list_of_numbers[1:]):
        if value > tmp_largest:
            tmp_largest = value
            i_largest = i + 1  # since starting at position 1
        else:
            continue
    # print("using largest_value_w_position")
    # print("""largest value is: {}\nposition index is: {}\n""".format(tmp_largest, i_largest))
    return tmp_largest, i_largest


numbers_list = [19, 41, 12, 63, 22]

largest_value_w_position(numbers_list)
largest_value_w_position_2(numbers_list)
