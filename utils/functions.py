# YOLO

import numpy

def file_to_list(file_path, separator, pop_final):
	with open(file_path) as input_file:
		input_text = input_file.read()
	input_list = input_text.split(separator)
	if pop_final:
		input_list.pop()
	return input_list

def list_to_numarray(input_list):
	# rows = len(input_list)
	# cols = len(input_list[0])

	# num_array = numpy.empty([rows,cols], dtype="U")

	# faster and cheaper to dynamically build the python array and convert the final product to numpy
	arr = []
	for i in input_list:
		arr.append(list(str(i)))
	
	return numpy.array(arr)

def count_around_3x3(input_num_array, char_to_count):
	arr = []
	arr.extend(input_num_array[1:2, 0::2].flatten().tolist())
	arr.extend(input_num_array[0::2, 1:2].flatten().tolist())
	arr.extend(input_num_array[0::2, 2:3].flatten().tolist())
	arr.extend(input_num_array[0::2, 0:1].flatten().tolist())
	return arr.count(char_to_count)
"""
for idx, x in numpy.ndenumerate(nums_array):
	print(idx, x)
"""

def arr_to_arrs(arr, separator):
	SPLIT = arr.index(separator)
	return [arr[0:SPLIT], arr[SPLIT+1:]]

def range_overlap(range1, range2):
	return not (range1.stop < range2.start or range2.stop < range1.start)

def merge_range(range1, range2):
	start = range1.start if range1.start < range2.start else range2.start
	stop = range1.stop if range1.stop > range2.stop else range2.stop
	return range(start, stop)
