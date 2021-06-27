def max(num1, num2, num3):
	nums = [num1, num2, num3]
	nums.sort()
	return nums[len(nums) - 1]

print(max(32, 65, 2))