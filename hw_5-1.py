# Author MB 10/21/2021

import random as rd

rd.seed(16)

# Question 1
a = rd.randint(30, 50)
print(a)

# Question 2
b = rd.randrange(2, 75, 2)
print(b)

# Question 3
c = rd.randrange(20, 30, 3)
print(c)

# Question 4
d = rd.randint(1, 8)
print(d)

# Question 5
e = rd.randint(1, 20)
print(e)

# Question 6
f = rd.choice(['cat', 'dog', 'sheep', 'cow', 'chicken', 'pig'])
print(f)

# Question 7
g = rd.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=4)
print(g)

# Question 8
j = rd.sample([1, 2, 3, 4, 5], k=5)
print(j)

# Question 9
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
n = rd.shuffle(cards)
print(n)

# Question 10
rd.seed(1942)
m = rd.randint(1, 1000)
print(m)
