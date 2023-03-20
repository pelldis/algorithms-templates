import sys


class QueueLIst:

    def __init__(self):
        self.queue = []
        self.head = 0
        self.tail = 0
        self.size = 0

    def put(self, x):
        self.queue.append(x)
        self.size += 1
        self.tail = 1

    def get(self):
        if self.size == 0:
            print("error")
            return None
        x = self.queue[self.head]
        self.head = (self.head + 1) % self.tail
        self.size -= 1
        self.queue.remove(x)
        print(x)

    def size(self):
        return self.size


def read_input():
    """Read from input and make list with numbers."""
    n = int(sys.stdin.readline().rstrip())
    commands = [0] * n
    # read string from input and make one list
    for i in range(n):
        commands[i] = sys.stdin.readline().rstrip().split()
    return commands


def main():
    commands = read_input()
    queue = QueueLIst()
    for command in commands:
        if command[0] == "get":
            queue.get()
        elif command[0] == "size":
            print(queue.size)
        elif command[0] == "put":
            queue.put(int(command[1]))


if __name__ == "__main__":
    main()
