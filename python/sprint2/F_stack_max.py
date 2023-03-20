class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            print("error")
            return "error"
        return self.items.pop()

    def get_max(self):
        if not self.items:
            return None
        return max(self.items)


def read_input():
    """Read from input and make list with numbers."""
    n = int(input())
    commands = [0] * n
    # read string from input and make one list
    for i in range(n):
        commands[i] = input().split()

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
