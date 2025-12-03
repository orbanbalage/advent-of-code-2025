# YOLO

def file_to_list(file_path, separator, pop_final):
	with open(file_path) as input_file:
		input_text = input_file.read()
	input_list = input_text.split(separator)
	if pop_final:
		input_list.pop()
	return input_list
