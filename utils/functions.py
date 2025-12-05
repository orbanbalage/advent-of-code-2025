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
