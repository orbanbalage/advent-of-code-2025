import sys
sys.path.append("../utils/")

import collections
from functions import file_to_list
from functions import arr_to_arrs

import numpy

input_sample_list = file_to_list("input-sample", "\n", pop_final=True)
input_list = file_to_list("input.txt", "\n", pop_final=True)

result = []

# arrs = arr_to_arrs(input_sample_list, "")
arrs = arr_to_arrs(input_list, "")

ranges_arr = arrs[0]
IDs_arr = arrs[1]

ranges = [range(int(x.split("-")[0]), int(x.split("-")[1])+1) for x in ranges_arr]
IDs = [int(x) for x in IDs_arr]

for ID in IDs:
	for r in ranges:
		if ID in r:
			# print(ID, r)
			result.append(ID)


print(len(set(result)))


