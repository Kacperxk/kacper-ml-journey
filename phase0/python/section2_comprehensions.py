from collections import Counter
import sys
import random

random.seed(42)

# Exercise 2.1


# Loop 1
result = []
for x in range(10):
    result.append(x ** 2)

comprehension = [x ** 2 for x in range(10)]
assert result == comprehension

# Loop 2
result = []
for x in range(20):
    if x % 2 == 0:
        result.append(x)

comprehension = [x for x in range(20) if x % 2 == 0]
assert result == comprehension

# Loop 3
words = ["hello", "world", "python", "ml"]
result = []
for word in words:
    result.append(word.upper())

comprehension = [word.upper() for word in words]
assert result == comprehension

# Loop 4
result = []
for i in range(3):
    for j in range(3):
        result.append((i, j))

comprehension = [(i, j) for i in range(3) for j in range(3)]
assert result == comprehension

# Loop 5
result = []
for i in range(5):
    for j in range(5):
        if i != j:
            result.append(i * j)

comprehension = [i * j for i in range(5) for j in range(5) if i != j]
assert result == comprehension


# Exercise 2.2


students = [
    ('Michal', 4.5),
    ('Anna', 5.0,),
    ('Piotr', 3.8,),
    ('Kasia', 4.2,)
]

grades = {name: grade for name, grade in students}

good_students = {name: grade for name, grade in students if grade >= 4}

first_letters = {name[0] for name, grade in students}

words = ["the", "quick", "brown", "fox", "the", "quick"]
freq = {word: words.count(word) for word in words}
freq = Counter(words) # different method (better)

original = {"a": 1, "b": 2, "c": 3}
inverted = {value: key for key, value in original.items()}


# Exercise 2.3


n = 1_000_000

list_comp = [x ** 2 for x in range(n)]
gen_expr = (x ** 2 for x in range(n))

print(sys.getsizeof(list_comp)) # Large - loads fully
print(sys.getsizeof(gen_expr)) # Tiny - stores generator state, waits for next()

gen = (x ** 2 for x in range(5))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# One more next() call would raise error StopIteration

total = sum(x ** 2 for x in range(1000))
assert total == 332833500

even_squares = list(x ** 2 for x in range(20) if x % 2 == 0)
print(even_squares)

any_divisible = any(x % 997 == 0 for x in range(1000))


# Exercise 2.4


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
words = ["alpha", "beta", "gamma", "delta"]

squares_comp = [x ** 2 for x in numbers]
squares_map = list(map(lambda x: x ** 2, numbers))
assert squares_comp == squares_map

odds_comp = [x for x in numbers if x % 2 != 0]
odds_filter = list(filter(lambda x: x % 2 != 0, numbers))
assert odds_comp == odds_filter

pairs_comp = [(word, len(word)) for word in words]
pairs_zip = list(zip(words, map(len, words)))
assert pairs_comp == pairs_zip

indexed_comp = [(i, w) for i, w in enumerate(words)]
indexed_enum = list(enumerate(words))
assert indexed_comp == indexed_enum

keys = ["a", "b", "c", "d"]
values = [1, 2, 3, 4]
d = dict(zip(keys, values))
print(d)
# When one list is longer, it cuts excess items from longer list to match shorter one
values = [1, 2]
d = dict(zip(keys, values))
print(d)



# Exercise 2.5


dataset = [
    ([random.gauss(0, 1) for _ in range(4)], random.randint(0,2)) for _ in range(100)
    ]

labels = [label for _, label in dataset]
features = [vector for vector, _ in dataset]

class_counts = {cls: sum(1 for _, label in dataset if label == cls) for cls in range(3)}
binary_dataset = [(feat, label) for feat, label in dataset if label != 2]

mini_batch = dataset[::10]
assert len(mini_batch) == 10

batches = [dataset[i:i+10] for i in range(0, 100, 10)]
flat = [sample for batch in batches for sample in batch]
assert flat == dataset