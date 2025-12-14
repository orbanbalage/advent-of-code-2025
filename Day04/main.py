import sys
sys.path.append("../utils/")

import collections
from functions import file_to_list
from functions import list_to_numarray
from functions import count_around_3x3

import numpy
from numpy.lib.stride_tricks import sliding_window_view

input_sample_list = file_to_list("input-sample", "\n", pop_final=True)
input_list = file_to_list("input.txt", "\n", pop_final=True)

result = 0

ROLL = "@"
ROLL_LIMIT = 4
WINDOW_DIM = 3

# nums_array = list_to_numarray(input_sample_list)
nums_array = list_to_numarray(input_list)

ARR_MAX_LEN = len(nums_array[0]) - 1

# corners:
# select only 0/n combos:
v_c = sliding_window_view(nums_array, (WINDOW_DIM-1,WINDOW_DIM-1))
corners = [ str(v_c[0][0][0][0]) == ROLL,
	str(v_c[0][-1][0][-1]) == ROLL,
	str(v_c[-1][0][-1][0]) == ROLL,
	str(v_c[-1][-1][-1][-1]) == ROLL
]

result += sum(corners)

# sides:
# vertical
v_v = sliding_window_view(nums_array, (WINDOW_DIM,WINDOW_DIM-1))

for x in v_v[:,0]:
	if x.flatten().tolist()[2] == ROLL:
		if x.flatten().tolist().count(ROLL) - 1 < ROLL_LIMIT:
			result += 1

for x in v_v[:,-1]:
	if x.flatten().tolist()[3] == ROLL:
		if x.flatten().tolist().count(ROLL) - 1 < ROLL_LIMIT:
			result += 1

# horizontal
v_h = sliding_window_view(nums_array, (WINDOW_DIM-1,WINDOW_DIM))

for x in v_h[0]:
	if x.flatten().tolist()[1] == ROLL:
		if x.flatten().tolist().count(ROLL) - 1 < ROLL_LIMIT:
			result += 1

for x in v_h[-1]:
	if x.flatten().tolist()[4] == ROLL:
		if x.flatten().tolist().count(ROLL) - 1 < ROLL_LIMIT:
			result += 1


# center, what is left:
v = sliding_window_view(nums_array, (WINDOW_DIM,WINDOW_DIM))
# always test the center for == ROLL first. [1][1] == ROLL.

for x in v:
	for y in x:
		if y.flatten().tolist()[4] == ROLL:
			if y.flatten().tolist().count(ROLL) - 1 < ROLL_LIMIT:
				result += 1

"""
for idx, x in numpy.ndenumerate(nums_array):
	lim_min = 0
	lim_max = len(nums_array[0]) - 1
	# print(idx, x)
	# print(nums_array[idx[0],idx[1]])
	if arr.count(ROLL) < ROLL_LIMIT:
		result += 1

# print(count_around_3x3(nums_array, "@"))
"""

print(result)
