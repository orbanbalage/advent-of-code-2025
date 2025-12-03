import sys
sys.path.append("../utils/")

import collections
from functions import file_to_list

input_sample_list = file_to_list("input-sample", "\n", pop_final=True)
input_list = file_to_list("input.txt", "\n", pop_final=True)

result = 0

# for i in input_sample_list:
for i in input_list:
	nums = list(str(i))
	# print(nums)
	max_0 = max(nums[:-1])
	max_0_index = nums.index(max_0)
	max_1 = max(nums[max_0_index+1:])
	result += int(max_0+max_1)

	
print(result)


