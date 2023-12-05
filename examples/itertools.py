import itertools


##      itertools Combinations      ##
characters = ['A', 'B', 'C']
combinations = list(itertools.combinations(characters, 2))
print(combinations)
# Output: [('A', 'B'), ('A', 'C'), ('B', 'C')]


##      itertools Permutations      ##
for perm in itertools.permutations([1, 2, 3]):
    print(perm)
# Output: (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)


##      itertools Product      ##
for pair in itertools.product("AB", [1, 2]):
    print(pair)
# Output: ('A', 1), ('A', 2), ('B', 1), ('B', 2)


##      itertools Cycle (indefinitely)      ##
count = 0
for item in itertools.cycle('AB'):
    if count > 5:
        break
    print(item)
    count += 1
# Output: 'A', 'B', 'A', 'B', 'A', 'B'