# 84377587


MATH_OPERATIONS = {
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x // y,
}


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.__items:
            raise IndexError("pop from empty stack")
        return self.__items.pop()


def read_input():
    """Read from input."""
    return input().split()


def main():
    stack = Stack()
    for item in read_input():
        if item not in MATH_OPERATIONS:
            stack.push(int(item))
        else:
            x2 = stack.pop()
            x1 = stack.pop()
            stack.push(MATH_OPERATIONS[item](x1, x2))
    print(stack.pop())


if __name__ == "__main__":
    main()
