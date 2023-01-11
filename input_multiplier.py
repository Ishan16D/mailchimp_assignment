import os
import random

# A script to create a larger input file

dirname = os.path.dirname(__file__)
input_filename = os.path.join(dirname, 'inputs/bigger_input.txt')

file = open(input_filename, 'a+')

for i in range(1000):
    random_list = []
    for i in range(0,1000):
        n = random.randint(1,100000)
        random_list.append(str(n))
    #print(len(random_list))
    line = random_list[0]
    for num in random_list[1:]:
        line += ' '
        line += num
    file.write(line)
    file.write('\n')

file.close()
# bigger_input.close()