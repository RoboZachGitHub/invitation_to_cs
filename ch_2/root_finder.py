# Schneider & Gersting
# Invitation to CS
# Ch. 2
# challenge work Problem 1
# basic root finder

def is_sign_different(a: float, b: float):
    if a >= 0.0 and b < 0.0:
        return True
    elif a < 0.0 and b >= 0.0:
        return True
    else:
        return False


def find_root(f_of_x, starting_x: float, step_x: float, accuracy_desired: float, max_attempts = 40):
    # a root is found when the sign of f_of_x changes from either
    # + to -, or - to +
    x = starting_x
    root = None
    attempts = 0
    while not root and attempts < max_attempts:
        attempts += 1
        x_right = x + step_x
        y_left = f_of_x(x)
        y_right = f_of_x(x_right)
        if is_sign_different(y_left, y_right):
            if step_x < accuracy_desired:
                print('root found at x={} within {} accuracy'.format(x ,accuracy_desired))
                print('f({}) = {}'.format(x, y_left))
                return x
            else:
                step_x = -1*step_x  # now search left to pin down the root at higher accuracy
                step_x = step_x*0.1 # reduce step distance to not over-step and for higher accuracy
        else:
            attempts += 1
        x = x_right
    print('max_attempts ({}) reached, and no root was found.'.format(max_attempts))
    return 0

def x_cubed(x: float = 0.0):
    return x**3

find_root(x_cubed, starting_x=-0.2, step_x=0.11, accuracy_desired=0.0000001, max_attempts=200000)



