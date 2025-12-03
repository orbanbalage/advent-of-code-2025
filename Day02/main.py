import sys
sys.path.append("../utils/")

import collections
from functions import file_to_list

input_sample_list = file_to_list("input-sample", ",", pop_final=False)
input_list = file_to_list("input.txt", ",", pop_final=False)

result = 0

# for i in input_sample_list:
for i in input_list:
	nums = i.split("-")
	# print(i)
	num_1 = int(nums[0])
	num_2 = int(nums[1])
	num_1_len = len(nums[0])
	num_2_len = len(nums[1])
	num_1_len_even = num_1_len % 2 == 0
	num_2_len_even = num_2_len % 2 == 0
	num_len_half = num_1_len // 2 if num_1_len_even else num_2_len // 2
	if num_1_len_even or num_2_len_even:
		# print(num_len_half, [*range(num_1, num_2 + 1)])
		# print(num_len_half, [a for a in range(num_1, num_2 + 1) if len(str(a)) % 2 == 0])
		num_array = [a for a in range(num_1, num_2 + 1) if len(str(a)) % 2 == 0]
		# print(num_array)
		# print(set([str(a)[0:num_len_half] for a in range(num_1, num_2 + 1) if len(str(a)) % 2 == 0]))
		digits = set([str(a)[0:num_len_half] for a in range(num_1, num_2 + 1) if len(str(a)) % 2 == 0])
		# print(digits)
		# print(sum([int(x+x) for x in digits if int(x+x) in num_array]))
		result += sum([int(x+x) for x in digits if int(x+x) in num_array])
	
print(result)


