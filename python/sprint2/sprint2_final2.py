# 84278869


MATH_OPERATIONS = {
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x // y,
}


class Stack:
    def __init__(self):
        self.__items = []
        self.__head = 0
        self.__tail = 0

    def __str__(self):
        return str(self.__items[-1])

    def push(self, item):
        self.__items.append(item)
        self.__items[self.__tail] = item
        self.__tail += 1

    def pop(self, item):
        x1 = self.__items[self.__tail - 2]
        x2 = self.__items.pop()
        self.__tail -= 1
        self.__items[self.__tail - 1] = MATH_OPERATIONS[item](x1, x2)

    def get_max(self):
        if not self.__items:
            return None
        return max(self.__items)


def read_input():
    """Read from input and make list with numbers."""
    calc_example = input().split()
    # read string from input and make one list
    return calc_example


def main():
    stack = Stack()
    for item in read_input():
        if item not in "*/-+":
            stack.push(int(item))
        else:
            stack.pop(item)
    print(stack)


if __name__ == "__main__":
    main()
