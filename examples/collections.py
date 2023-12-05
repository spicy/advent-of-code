from collections import OrderedDict, Counter


##      collections Ordered Dictionary      ##
ord_dict = OrderedDict([('banana', 3), ('apple', 4), ('pear', 1), ('orange', 2)])
for key, value in ord_dict.items():
    print(key, value)
# Output: 'banana' 3, 'apple' 4, 'pear' 1, 'orange' 2


##      collections Counter      ##
fruits = ['apple', 'banana', 'apple', 'orange']
fruit_count = Counter(fruits)
print(fruit_count)
# Output: Counter({'apple': 2, 'banana': 1, 'orange': 1})