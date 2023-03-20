import sys


def solution(n):
    if n == 1 or n == 0:
        return 1
    return solution(n - 1) + solution(n - 2)


def read_input():
    return int(sys.stdin.readline().strip())


def main():
    print(solution(read_input()))


if __name__ == "__main__":
    main()
