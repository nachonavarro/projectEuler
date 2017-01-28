import math, datetime
from collections import Counter
from fractions import gcd

# 1.
# Find the sum of all the multiples of 3 or 5 below 1000.
def multiples_3_5(n):
	list_3  = [3  * x for x in range(1, (n - 1) // 3  + 1)]
	list_5  = [5  * x for x in range(1, (n - 1) // 5  + 1)]
	list_15 = [15 * x for x in range(1, (n - 1) // 15 + 1)]
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

def proper_factors(n):    
    fact = set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    return [f for f in fact if f != n]

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

# 11.
# What is the greatest product of four adjacent numbers in the same direction 
# (up, down, left, right, or diagonally) in the 20×20 grid?
grid = []
with open('grid.txt') as f:
	for line in f:
		row = []
		for x in line.split():
			row.append(int(x))
		grid.append(row)
def largest_product_in_grid(grid):
	largest = 0
	boundary_up   = 3
	boundary_down = 16
	# Brute force
	for i in range(20):
		for j in range(20):
			up = down = left = right = 0
			left_up = left_down = right_up = right_down = 0
			if i <= boundary_down:
				down  = grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]
			if i >= boundary_up:
				up    = grid[i][j] * grid[i - 1][j] * grid[i - 2][j] * grid[i - 3][j]
			if j <= boundary_down:
				right = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
			if j >= boundary_up:
				left  = grid[i][j] * grid[i][j - 1] * grid[i][j - 2] * grid[i][j - 3]
			if i >= boundary_up and j >= boundary_up:
				left_up = grid[i][j] * grid[i - 1][j - 1] * grid[i - 2][j - 2] * grid[i - 3][j - 3]
			if i <= boundary_down and j >= boundary_up:
				left_down = grid[i][j] * grid[i + 1][j - 1] * grid[i + 2][j - 2] * grid[i + 3][j - 3]
			if i >= boundary_up and j <= boundary_down:
				right_up = grid[i][j] * grid[i - 1][j + 1] * grid[i - 2][j + 2] * grid[i - 3][j + 3]
			if i <= boundary_down and j <= boundary_down:
				right_down = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
			largest = max(up, down, right, left, left_up, left_down, right_up, right_down, largest)
	return largest
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

# 14.
# Which starting number, under one million, produces the longest chain
# of a Collatz sequence?
def collatz_sequence(n):
	seq = [n]
	while n > 1:
		n = n / 2 if n % 2 == 0 else 3 * n + 1
		seq.append(n)
	return seq

def longest_collatz_sequence_under(n):
	longest = 0
	starting_number = 0
	for i in range(n - 1, 0, -1):
		length = len(collatz_sequence(i))
		if length > longest:
			longest = length
			starting_number = i
	return starting_number

# 16.
# What is the sum of the digits of the number 21000?
def sum_digits(num):
	return sum([int(x) for x in str(num)])

# 17.
# If all the numbers from 1 to 1000 (one thousand) 
# inclusive were written out in words, how many letters would be used?
def letter_counts():
	d = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',
			 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen',
			 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen',
			 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty',
			 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred'}
	count = 0
	# 1 to 99
	for num in range(1, 100):
		if num in d:
			count += len(d[num])
		else:
			tens   = int(str(num)[0]) * 10
			ones   = int(str(num)[1])
			count += len(d[tens]) + len(d[ones])
	
	# 100 to 999
	for num in range(100, 1000):
		hundreds      = int(str(num)[0]) 
		tens          = int(str(num)[1]) * 10
		ones          = int(str(num)[2])
		tens_and_ones = int(str(num)[1:3])
		# Account for 'and'
		if tens_and_ones in d and tens_and_ones:
			count += len(d[hundreds]) + len('hundredand') + len(d[tens_and_ones])
		elif tens and ones:
			count += len(d[hundreds]) + len('hundredand') + len(d[tens]) + len(d[ones])
		else:
			count += len(d[hundreds]) + len('hundred') + len(d[tens]) + len(d[ones])
	
	# 1000
	thousand = 'onethousand'
	count += len(thousand)
	return count

# 18.
# Find the maximum total from top to bottom of a triangle.
# Notes: keep shrinking the triangle until there is only one element.
# Input is in the format: [[1,2,3], [4,5], [6]]
def maximum_path_sum(mat):
	height = 0
	while height < len(mat) - 1:
		row = mat[height]
		width = len(row)
		updated_row = []
		for i in range(width - 1):
			updated_row.append(max(row[i], row[i + 1]))
		mat[height + 1] = [x + y for x,y in zip(mat[height + 1], updated_row)]
		height += 1
	# We have propagated the sum up the triangle, hence the list containing
	# the root has the answer, i.e., the first element of the last list in mat.
	return mat[-1][0] 

# 19.
# How many Sundays fell on the first of the month during the twentieth century 
# (1 Jan 1901 to 31 Dec 2000)?
def counting_sundays_between(begin_year, end_year):
	sundays = 0
	for year in range(begin_year, end_year + 1):
		for month in range(1, 13):
			if datetime.datetime(year, month, 1).weekday() == 6:
				sundays += 1
	return sundays

# 20.
# Find the sum of the digits in the number 100!
def factorial_digit_sum(n):
	temp = [1, 1]
	for i in range(1, n + 1):
		temp[0], temp[1] = temp[1], i * temp[1]
	fact = temp[1]
	return sum([int(x) for x in str(fact)])

# 21.
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
# which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and b 
# are an amicable pair and each of a and b are called amicable numbers.
# Evaluate the sum of all the amicable numbers under 10000.
def is_amicable(n):
	twin = sum(proper_factors(n))
	return sum(proper_factors(twin)) == n and n != twin

def sum_of_amicables():
	amicables = []
	for n in range(2, 10001):
		if is_amicable(n):
			amicables.append(n)
	return sum(amicables)

# 22.
# Working out the alphabetical value for each name in names.txt, 
# multiply this value by its alphabetical position in the list to obtain a name score.
# What is the total of all the name scores in the file?
# names_list = []
# with open('names.txt') as f:
# 	for line in f:
# 		for name in line.split(","):
# 			names_list.append(name.strip('"'))
def names_scores(names):
	names.sort()
	alphabet = {chr(n).upper() : n % 32 for n in range(97, 97 + 26)}
	total = 0
	for i,name in enumerate(names):
		weight = sum(map(lambda x: alphabet[x], name))
		total += (i + 1) * weight
	return total
		
# 24.
# What is the millionth lexicographic permutation of the digits 
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
# Don't take credit for helper function.
def next_permutation(arr):
  # Find non-increasing suffix
  arr = list(arr)
  i = len(arr) - 1
  while i > 0 and arr[i - 1] >= arr[i]:
      i -= 1
  if i <= 0:
      return False
  
  # Find successor to pivot
  j = len(arr) - 1
  while arr[j] <= arr[i - 1]:
      j -= 1
  arr[i - 1], arr[j] = arr[j], arr[i - 1]
  
  # Reverse suffix
  arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
  return "".join(arr)

def millionth_lexicographic():
	counter = 1
	curr    = '0123456789'
	while counter < 1000000:
		curr = next_permutation(curr)
		counter += 1
	return curr

# 25.
# What is the index of the first term in the Fibonacci 
# sequence to contain 1000 digits?
def fib_index_digits(n):
	temp = [1, 1]
	idx  = 1   
	while True:
		temp[0], temp[1] = temp[1], sum(temp)
		if len(str(temp[0])) == n:
			return idx + 1
		idx += 1

# 30.
# Find the sum of all the numbers that can be written as the sum of 
# fifth powers of their digits.

def fifth_power_sum():
	# For fast access
	surprising = []
	d = {i:i**5 for i in range(10)}
	limit = 6 * d[9] # Above this limit, no number can work
	for i in range(100, limit):
		total = 0
		for x in [int(j) for j in str(i)]:
			total += d[x]
		if total == i:
			surprising.append(i)
	return sum(surprising)

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
	for key, values in d.items():
		for value in values:
			if is_curious(key, value):
				curious_fractions.append((key, value))
	return
