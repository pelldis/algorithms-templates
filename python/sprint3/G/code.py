def str_greater(a, b):
    return str(a) + str(b) > str(b) + str(a)


def solution(arr, n):
    dct = {0: [], 1: [], 2: []}
    for value in arr:
        dct[value].append(value)
    return dct[0] + dct[1] + dct[2]


def read_input():
    n = int(input())
    arr = list(map(int, input().split()))
    return arr, n


def main():
    print(*solution(*read_input()))


if __name__ == "__main__":
    main()
