nums = [3, 6, 9, 12]
new = int(input('Enter another number: '))
nums.append(new)
total = 0
for i in nums:
	total += i
print('The total is %d' %total)
