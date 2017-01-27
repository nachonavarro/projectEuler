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

# 4.
# Find the largest palindrome made from the product of two 3-digit numbers.
# Notes: I've checked only from 999 to 900, it worked out.
def largest_palindrome():
	# Create a dict like so:
	# {999: [999, 998, ... , 900],
	#  998: [998, 997, ..., 900],
	#  997: [997, 996, ..., 900]}
	d = {}
	for i in range(999, 900, -1):
		d[i] = [j for j in range(i, 900, -1)]
	largest = 0
	
	# Look if palindrome.
	for key in d:
		for m in d[key]:
			curr = m * key
			to_str = str(curr)
			if to_str == to_str[::-1] and curr > largest:
				largest = curr
	return largest
	
# 5.
# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
 
def evenly_divisible_until(n):
	list_factors = factors(n)
	# Only need to check on non-factors of 20.
	check_nums = filter(lambda x: x not in list_factors, range(1, n + 1))
	num = n
	while True:
		divisible = True
		for i in check_nums:
			if num % i != 0:
				divisible = False
				break
		if divisible:
			return num
		else:
			num += n
			
# 6.
# Find the difference between the sum of the squares of the first one 
# hundred natural numbers and the square of the sum.
def sum_square_difference(n):
	sum_of_squares = n * (n + 1) * (2 * n + 1) / 6
	square_of_sum  = sum(range(n + 1)) ** 2
	return square_of_sum - sum_of_squares