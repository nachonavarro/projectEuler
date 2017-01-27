import math

# 1.
# Find the sum of all the multiples of 3 or 5 below 1000.
def multiples_3_5(n):
	list_3  = [3  * x for x in range(1, (n - 1) // 3  + 1)]
	list_5  = [5  * x for x in range(1, (n - 1) // 5  + 1)]
	list_15 = [15 * x for x in range(1, (n - 1) // 15 + 1)]
	print(list_3, list_5, list_15)
	return sum(list_3) + sum(list_5) - sum(list_15)

# 2.
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.
def sum_even_fib(n):
	temp     = [1, 1]
	even_sum = 0
	while temp[1] < n:
		temp[0], temp[1] = temp[1], sum(temp)
		if temp[0] % 2 == 0:
			even_sum += temp[0]
		print(temp)
	return even_sum

# 3.
# What is the largest prime factor of the number 600851475143 ?
def is_prime(n):
	if n % 2 == 0 and n > 2: 
		return False
	return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def largest_prime_factor(n):
	curr = int(math.sqrt(n))
	# Consider only odd numbers.
	if curr % 2 == 0:
		curr -= 1
		
	while curr > 1:
		if n % curr == 0:
			if is_prime(curr):
				return curr
		curr -= 2