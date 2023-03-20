import sys


class Node:
    def __init__(self, value, max_value):
        self.value = value
        self.max_value = max_value


class Stack:
    def __init__(self):
        self.items = []
        self.max = None

    def push(self, item):
        if self.max is None:
            self.max = item
            item = Node(item, None)
            self.items.append(item)
        elif self.max < item:
            new_item = Node(item, self.max)
            self.max = item
            self.items.append(new_item)
        elif self.max >= item:
            self.items.append(Node(item, self.max))

    def pop(self):
        if not self.items:
            print("error")
            return "error"
        self.max = self.items.pop().max_value
        return

    def get_max(self):
        if not self.items:
            return None
        return self.max


def read_input():
    """Read from input and make list with numbers."""
    n = int(sys.stdin.readline().rstrip())
    commands = [0] * n
    # read string from input and make one list
    for i in range(n):
        commands[i] = sys.stdin.readline().rstrip().split()
    return commands


def main():
    stack = Stack()
    for command in read_input():
        if command[0] == "get_max":
            print(stack.get_max())
        elif command[0] == "pop":
            stack.pop()
        elif command[0] == "push":
            stack.push(int(command[1]))


if __name__ == "__main__":
    main()
