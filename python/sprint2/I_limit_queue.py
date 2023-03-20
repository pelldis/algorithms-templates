import sys


class MyQueueSized:

    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def push(self, x):
        if self.size != self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            print("error")

    def pop(self):
        if self.size == 0:
            print(None)
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        print(x)

    def peek(self):
        if self.size == 0:
            print(None)
        else:
            print(self.queue[self.head])

    def size(self):
        return self.size


def read_input():
    """Read from input and make list with numbers."""
    n = int(sys.stdin.readline().rstrip())
    commands = [0] * n
    max_size = int(sys.stdin.readline().rstrip())
    # read string from input and make one list
    for i in range(n):
        commands[i] = sys.stdin.readline().rstrip().split()
    return commands, max_size


def main():
    commands, max_size = read_input()
    queue = MyQueueSized(max_size)
    for command in commands:
        if command[0] == "peek":
            queue.peek()
        elif command[0] == "size":
            print(queue.size)
        elif command[0] == "push":
            queue.push(int(command[1]))
        elif command[0] == "pop":
            queue.pop()


if __name__ == "__main__":
    main()
