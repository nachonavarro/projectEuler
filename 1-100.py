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
	
# 7.
# What is the 10 001st prime number?
def prime_number(n):
	if n == 1:
		return 2
	curr_num = 3
	prime_count = 2
	while prime_count < n:
		curr_num += 2
		if is_prime(curr_num):
			prime_count += 1
	return curr_num
	
# 8.
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. 
# What is the value of this product?
def largest_product_in_series(n, consecutive):
	num_digits  = len(str(n))
	digits     = [int(i) for i in str(n)]
	max_product = 0
	i = 0
	while i <= num_digits - consecutive:
		max_here = 1
		for j in range(consecutive):
			if digits[i + j] == 0:
				i += j # Skip.
				break
			else:
				max_here *= digits[i + j]
			max_product = max(max_product, max_here)
		i += 1
	return max_product

# 9.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# Notes: if a^2 + b^2 = c^2 and a + b + c = 1000, substitute for c and simplify.
def special_pythagorean_triplet():
	# a and b need to satisfy the following relation:
	# a = (500000 - 1000 * b) / (1000 - b)
	# Hence, (500000 - 1000 * b) mod (1000 - b) has to be 0. There are only a few choices for b then.
	possibles = []
	for i in range(1, 1000):
		if (500000 - 1000 * i) % (1000 - i) == 0:
			possibles.append(i)
	for i in possibles:
		a = (500000 - 1000 * i) / (1000 - i)
		b = i
		c = int(math.sqrt(a ** 2 + b ** 2))
		if a + b + c == 1000:
			return a * b * c

# 10.
# Find the sum of all the primes below two million.
def fast_primes(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def sum_of_all_primes_below(n):
	return sum(fast_primes(n))


# 12.
# What is the value of the first triangle number to have over 
# five hundred divisors?
def triangle_number_over_n_divisors(n):
	curr = 1
	idx  = 2
	while len(factors(curr)) < n:
		curr += idx
		idx += 1
	return curr

# 13.
# Work out the first ten digits of the sum of the following 
# one-hundred 50-digit numbers.
def large_sum(list_numbers):
	return sum(list_numbers)

# 16.
# What is the sum of the digits of the number 21000?
def sum_digits(num):
	return sum([int(x) for x in str(num)])
	
# 20.
# Find the sum of the digits in the number 100!
def factorial_digit_sum(n):
	temp = [1, 1]
	for i in range(1, n + 1):
		temp[0], temp[1] = temp[1], i * temp[1]
	fact = temp[1]
	return sum([int(x) for x in str(fact)])
	
# 25.
# What is the index of the first term in the Fibonacci 
# sequence to contain 1000 digits?
def fib_index_digits(n):
	temp = [1, 1]
	idx  = 1   
	while True:
		print(temp[0])
		temp[0], temp[1] = temp[1], sum(temp)
		if len(str(temp[0])) == n:
			return idx + 1
		idx += 1

# 33.
# There are exactly four non-trivial examples of this type of fraction, 
# less than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, 
# find the value of the denominator.
def is_curious(numerator, denominator):
	value = numerator / float(denominator)
	numerator_without_tens   = int(str(numerator)[0])
	numerator_without_ones   = int(str(numerator)[1])
	denominator_without_tens = int(str(denominator)[0])
	denominator_without_ones = int(str(denominator)[1])
	
	if numerator_without_ones == denominator_without_ones:
		return numerator_without_tens / float(denominator_without_tens) == value
	elif numerator_without_ones == denominator_without_tens:
		return numerator_without_tens / float(denominator_without_ones) == value
	elif numerator_without_tens == denominator_without_ones:
		return numerator_without_ones / float(denominator_without_tens) == value
	elif numerator_without_tens == denominator_without_tens:
		return numerator_without_ones / float(denominator_without_ones) == value
	
def digit_cancelling_fractions():
	# Initialize dict matching each numerator with all possible denominators, e.g.
	# {11:[12,13, ... , 99], 12:[13, ..., 99], ... , 97: [98, 99], 98: [99]}
	d = {}
	curious_fractions = []
	for i in range(11, 100):
		if i % 10 != 0:
			d[i] = []
			for j in range(i, 100):
				first_digit = str(i)[0]
				second_digit = str(i)[1]
				if j != i and '0' not in str(j) and (first_digit in str(j) or second_digit in str(j)):
					d[i].append(j)
	# print(d)
	for key, values in d.items():
		for value in values:
			if is_curious(key, value):
				curious_fractions.append((key, value))
	return
	