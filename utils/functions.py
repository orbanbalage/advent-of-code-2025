# YOLO

def file_to_list(file_path, separator):
	with open(file_path) as input_file:
		input_text = input_file.read()
	input_list = input_text.split(separator)
	input_list.pop()
	return input_list
