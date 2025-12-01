import sys
sys.path.append("../utils/")

import collections
#from utils.input import file_to_list
from input_functions import file_to_list

input_sample_list = file_to_list("input-sample")
input_list = file_to_list("input.txt")

START = 50
result = 0

dial = collections.deque(range(100), maxlen=100)

dial.rotate(START)

# for i in input_sample_list:
for i in input_list:
	sign = 1 if i[0] == "R" else -1
	dial.rotate(sign * int(i[1:]))
	# print(dial[0])
	if dial[0] == 0:
		result = result + 1

print(result)
