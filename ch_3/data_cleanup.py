# Schneider & Gersting
# Invitation to CS
# data cleanup algorithms from Ch. 3
# Ch. 3: the efficiency of algorithms

from sorting_algorithms import swap_list_positions


def shuffle_left(data_to_clean: list):
    tmp = data_to_clean
    for i, elem in enumerate(tmp):
        if elem == 0:
            for j, elem_b in enumerate(tmp[i:-1], start=i):
                tmp = swap_list_positions(tmp, j, j+1)
    return tmp


def copy_over(data_to_clean: list):
    tmp = data_to_clean
    tmp_clean = []
    for val in tmp:
        if val != 0:
            tmp_clean.append(val)
    return tmp_clean


def converging_pointers(data_to_clean: list):
    tmp = data_to_clean
    legit = len(tmp)
    i = 0
    j = len(data_to_clean) - 1
    while i <= j:
        if tmp[i] == 0:
            tmp[i] = tmp[j]
            legit -= 1
            j -= 1
        i += 1
    return data_to_clean[:legit]


test_list = [1, 2, 3, 4, 0, 1, 0, 9, 0, 3, 2]

# x = shuffle_left(test_list)
# y = copy_over(test_list)
# z = converging_pointers(test_list)
# print(x)
# print(y)
# print(z)
