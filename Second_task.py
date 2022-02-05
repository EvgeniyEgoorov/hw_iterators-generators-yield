def flat_generator(data):
    for els in data:
        for el in els:
            yield el


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


flat_list = [item for item in flat_generator(nested_list)]
print(flat_list)

