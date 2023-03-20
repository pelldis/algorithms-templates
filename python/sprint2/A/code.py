import sys


def solution(lst, n, m):
    for i in range(m):
        print(*lst[i::m])
    return


def read_input():
    """Read from input and make list with numbers."""
    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())
    lst = []
    for i in range(n):
        lst += list(map(int, sys.stdin.readline().strip().split()))
    return lst, n, m


def main():
    solution(*read_input())


if __name__ == "__main__":
    main()
