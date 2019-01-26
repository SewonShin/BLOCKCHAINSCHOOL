import random

print(random.random())
print(random.uniform(10, 20))
print(random.randrange(10))
print(random.randrange(0, 101, 2))
print(random.choice(['a', 'b', 'c']))
a = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(a)
print(a)