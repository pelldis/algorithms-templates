# 84278470


class EmptyStack(Exception):
    ...


class FullStack(Exception):
    ...


class Deque:
    """Queue with limit size."""
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__queue = [None] * self.__max_size
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def swap_cursor(self, cursor):
        return cursor % self.__max_size

    def push_back(self, x):
        """Add element to the end."""
        if self.__size != self.__max_size:
            self.__queue[self.__tail] = x
            self.__tail = self.swap_cursor(self.__tail + 1)
            self.__size += 1
        else:
            raise FullStack("Stack is full")

    def pop_back(self):
        """Remove and print element from the end."""
        if self.__size == 0:
            raise EmptyStack("Stack is empty")
        x = self.__queue[self.__tail - 1]
        self.__queue[self.__tail - 1] = None
        self.__tail = self.swap_cursor(self.__tail - 1)
        self.__size -= 1
        return x

    def push_front(self, x):
        """Add element to the beginning."""
        if self.__size != self.__max_size:
            self.__queue[self.__head - 1] = x
            self.__head = self.swap_cursor(self.__head - 1)
            self.__size += 1
        else:
            raise FullStack("Stack is full")

    def pop_front(self):
        """Remove element from the beginning."""
        if self.__size == 0:
            raise EmptyStack("Stack is empty")
        x = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = self.swap_cursor(self.__head + 1)
        self.__size -= 1
        return x


def read_input():
    """Read from input and make list with numbers."""
    n = int(input())
    commands = [0] * n
    max_size = int(input())
    # read string from input and make one list
    for i in range(n):
        commands[i] = input()
    return commands, max_size


def use_deque(stack, command):
    """Run deque methods."""
    cmd, *arg = command.split()
    try:
        method = getattr(stack, cmd)
        return method(*arg)
    except EmptyStack:
        print("error")
    except FullStack:
        print("error")


def main():
    commands, max_size = read_input()
    queue = Deque(max_size)
    for command in commands:
        result = use_deque(queue, command)
        if result is not None:
            print(result)


if __name__ == "__main__":
    main()
