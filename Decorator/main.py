import time
import datetime
import os
from collections.abc import Iterable


def logger(file_name):
    def _loger(out_func):
        def inner_func(*args, **kwargs):
            start = time.time()
            result = out_func(*args, **kwargs)
            path = f'{os.getcwd()}/{file_name}'
            data = f'--- Имя функции: {out_func.__name__}, ' \
                   f'Аргументы функции: {args} {kwargs}, ' \
                   f'Дата вызова: {datetime.date.today()}, ' \
                   f'Время выполнения: {time.time() - start}, ' \
                   f'Результат выполнения: {result}'
            with open(path, 'a', encoding='utf-8') as f:
                f.write(data + '\n')
            return result

        return inner_func

    return _loger


def main():
    @logger('logfile.txt')
    def mult(a, b):
        return a ** b

    nested_list_2 = [None, True,
                     ['a', {0, 6, 7, '4', (5, True, 7,)}, 'c'],
                     ['d', [5], 'f', 'h', False],
                     [1, ['a', ['a', 'n', ['a', 'hhh', ['a', 'b', ['a', 'uty', 'c']]]], 'c'], None],
                     ]

    @logger('logfile.txt')
    def flat_generator(sequence):
        for element in sequence:
            if isinstance(element, Iterable) and not isinstance(element, str):
                yield from flat_generator(element)
            else:
                yield element

    for i in range(1, 5):
        mult(i, i ** 2)

    flat_generator(nested_list_2)


if __name__ == '__main__':
    main()
