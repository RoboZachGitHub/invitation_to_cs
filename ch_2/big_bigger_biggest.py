# Schneider & Gersting
# Invitation to CS
# Ch. 2.3.3

# find largest value in a list
# print its value and its position in the list

def largest_value_w_position(list_of_numbers: list):
    largest = 0
    i_largest = 0
    for i, value in enumerate(list_of_numbers):
        if value > largest:
            largest = value
            i_largest = i
        else:
            continue
    print("using largest_value_w_position")
    print("""largest value is: {}\nposition index is: {}\n""".format(largest, i_largest))
    return largest, i_largest


def largest_value_w_position_2(numbers_list: list):
    # same as largest_value_w_position, but using a while loop
    largest = 0
    i_largest = 0
    i = 0
    while i < len(numbers_list):
        value = numbers_list[i]
        if value > largest:
            largest = value
            i_largest = i
            i += 1
        else:
            i += 1

    print("using largest_value_w_position_2")
    print("""largest value is: {}\nposition index is: {}\n""".format(largest, i_largest))
    return largest, i_largest

numbers_list = (19, 41, 12, 63, 22)

largest_value_w_position(numbers_list)
largest_value_w_position_2(numbers_list)

