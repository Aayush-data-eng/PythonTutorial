# # Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
from collections import deque


class Stack:
    def __init__(self):
        self.container: deque[str] = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def reverseInputString(string):
    # string = string[::-1] # This is throught string slicing
    # return string

    stack = Stack()
    revstring = ""

    for char in string:
        stack.push(char)

    while stack.size() != 0:
        revstring += stack.pop()

    return revstring


if __name__ == "__main__":
    print (reverseInputString("We will conquere COVI-19"))