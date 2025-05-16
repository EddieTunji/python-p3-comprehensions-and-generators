squared_minus_one = list()

for n in range(1, 11):
    squared_minus_one.append((n ** 2) -1)

print(squared_minus_one)

squared_minus_one =[((n ** 2) -1) for n in range (1, 11)]
print(squared_minus_one)

squared_lc = [(n ** 2) for n in range (1, 4)]
print(squared_lc)
squared_ge = (n ** 2 for n in range (1, 6))
print(squared_ge)

import sys

list_comprehension = [n for n in range(100000)]
generator_expression = (n for n in range (100000))

sys.getsizeof(list_comprehension)
sys.getsizeof(generator_expression)