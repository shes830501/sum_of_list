# python 內建sum直接運算
def sum_of_list(numbers):
	return sum(numbers)
print(sum_of_list([1, 2, 3]))

#設三個parameters
def sum_of_list(x, y, z):
	return x + y + z
print(sum_of_list(1, 2, 3))

#for loop
def sum_of_list(numbers):
	sum = 0
	for num in numbers:
		sum = sum + num
	return sum
print(sum_of_list([1, 2, 3]))