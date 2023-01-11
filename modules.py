import numpy as np


def get_first_checksum(line : np.ndarray):

    # Calculate max and min values then get difference
    max_val = line.max()
    min_val = line.min()
    return max_val-min_val


def get_second_checksum(line: np.ndarray):
    # Start with 0 for each line
    div_result = 0

    # Iterate over numbers in the array as divisors
    for i in line:

        # Remove number being used as it will divide itself
        temp_line = np.delete(line, np.where(line == i)[0][0])

        # Calculate remainder using all other numbers as dividend
        rem_arr = np.remainder(temp_line, i)

        # Check if any numbers divide cleanly (remainder of 0)
        if len(np.where(rem_arr == 0)[0]) >0:

            # Get the first dividend for i
            first_div_ind = np.where(rem_arr == 0)[0][0]

            # Incremement by the result of the found dividend and divisor
            div_result += int(np.divide(temp_line[first_div_ind], i))

            # End loop when pair is found
            break

    return div_result

def catch_invalid(input):

    # Cast input strings from text file as integers for calculation and throw an error if a string cannot be cast as an integer
    try:
        input = int(input)
    except ValueError as err:
        print(f'Invalid input character. Unable to cast {input} as int. Please ensure input characters are numeric.')
        exit()
    return input
