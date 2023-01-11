# Imports and set up
import numpy as np
import csv
import os
import time
from modules import get_first_checksum, get_second_checksum, catch_invalid

dirname = os.path.dirname(__file__) + '/inputs'
input_file = input('Please enter the filename with extension you would like to test:')
filename = os.path.join(dirname, input_file)

# Initializing checksum values
checksum_minmax = 0
checksum_div = 0

# Reading the file
start = time.time()
line_count = 0
with open(filename) as file:
    tsv_file = csv.reader(file, delimiter='\t')

    for line in tsv_file:
        line_count += 1
        # Breaking up the lines into lists

        line = line[0].split(' ')

        # Throw an error if an input character in non numeric (or tab is not delimiter)
        line = [catch_invalid(num) for num in line]

        # Convert list to numpy array
        line = np.asarray(line)

        # Calculate checksum values
        try:

            checksum_minmax += get_first_checksum(line)
            checksum_div += get_second_checksum(line)
            #print(f'Done calculating checksums for row {line_count}')
        except Exception as err:
            print(err)
            print(f'Error occured on line {line_count}')


end = time.time()
print(f'The first checksum is {checksum_minmax}')
print(f'The second checksum is {checksum_div}')
print(f'Calculations took {end-start} s')
