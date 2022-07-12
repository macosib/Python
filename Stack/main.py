from typing import List
from collections import deque


class Stack:

    def __init__(self):
        self.stack = deque()
        # self.stack = []

    def isempty(self):
        return len(self.stack) == 0

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def check_bracket(bracket_sequence: str) -> str:
    stack_obj = Stack()
    flag = True
    for bracket in bracket_sequence:
        if bracket in '({[':
            stack_obj.push(bracket)
        elif stack_obj.isempty():
            flag = False
            break
        elif bracket == ')' and stack_obj.peek() == '(':
            stack_obj.pop()
        elif bracket == '}' and stack_obj.peek() == '{':
            stack_obj.pop()
        elif bracket == ']' and stack_obj.peek() == '[':
            stack_obj.pop()
        else:
            flag = False
            break
    return ['Несбалансированно', 'Сбалансированно'][all([flag, not stack_obj.size()])]


def main():
    test_data = ['[[{())}]', '((({{}})))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}']
    for test_case in test_data:
        print(f'Последовательность: {test_case}  ---> {check_bracket(test_case)}')

    'Задача из лекции через цикл'
    nums = [3, 2, 4]
    target = 6

    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            for index1, value1 in enumerate(nums):
                for index2, value2 in enumerate(nums[index1 + 1:], index1 + 1):
                    if value2 == target - value1:
                        return [index1, index2]


if __name__ == '__main__':
    main()
