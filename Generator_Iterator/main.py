import functools
import operator
from iteration_utilities import deepflatten
from collections.abc import Iterable

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]
''' Задание 1'''


class FlatIterator:

    def __init__(self, any_list):
        self.any_list = self.__unpacking(any_list)

    @staticmethod
    def __unpacking(any_list):
        'Несколько вариантов реализации:'
        # return [element for lst in any_list for element in lst]
        # return functools.reduce(operator.concat, any_list)
        # return list(itertools.chain.from_iterable(any_list))
        return list(deepflatten(any_list, ignore=str))

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.any_list):
            raise StopIteration
        else:
            return self.any_list[self.cursor]


print('Задание 1')
for item in FlatIterator(nested_list):
    print(item)
    #
flat_list = [item for item in FlatIterator(nested_list)]

print(flat_list)
print()
#
'''Задание 2'''


def flat_generator(any_list):
    for lst in any_list:
        for element in lst:
            yield element


print('Задание 2')
for item in flat_generator(nested_list):
    print(item)
    #
flat_list = [item for item in flat_generator(nested_list)]

print(flat_list)
print()

'''Задание 3'''

nested_list = [None, True,
               ['a', {0, 6, 7, '4', (5, True, 7,)}, 'c'],
               ['d', [5], 'f', 'h', False],
               [1, ['a', ['a', 'n', ['a', 'hhh', ['a', 'b', ['a', 'uty', 'c']]]], 'c'], None],
               ]


class FlatIterator:

    def __init__(self, any_list):
        self.any_list = self.__unpacking(any_list)

    'Вариант 1'
    # @staticmethod
    # def __unpacking(sequence):

    #     res = []
    #     for element in sequence:
    #         if isinstance(element, Iterable) and not isinstance(element, str):
    #             res.extend(FlatIterator.__unpacking(element))
    #         else:
    #             res.append(element)
    #     return res

    'Вариант 2'
    @staticmethod
    def __unpacking(sequence):
        return list(deepflatten(sequence, ignore=str))

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.any_list):
            raise StopIteration
        else:
            return self.any_list[self.cursor]


print('Задание 3')
for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)
print()

'''Задание 4'''


def flat_generator(sequence):
    for element in sequence:
        if isinstance(element, Iterable) and not isinstance(element, str):
            yield from flat_generator(element)
        else:
            yield element


print('Задание 4')
for item in flat_generator(nested_list):
    print(item)
    #
flat_list = [item for item in flat_generator(nested_list)]
print(flat_list)
