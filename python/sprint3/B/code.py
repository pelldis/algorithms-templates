def solution(n, prefix, lst, k):
    dct = {
        "2": 'abc',
        "3": 'def',
        "4": 'ghi',
        "5": 'jkl',
        "6": 'mno',
        "7": 'pqrs',
        "8": 'tuv',
        "9": 'wxyz'
    }
    if n == 0:
        print(prefix, end=" ")
    else:
        solution(n - 1, prefix + dct[lst[k]][0], lst, k + 1)
        solution(n - 1, prefix + dct[lst[k]][1], lst, k + 1)
        solution(n - 1, prefix + dct[lst[k]][2], lst, k + 1)
        if len(dct[lst[k]]) == 4:
            solution(n - 1, prefix + dct[lst[k]][3], lst, k + 1)


def read_input():
    return input()


def main():
    numbers = read_input()
    solution(len(numbers), "", numbers, 0)


if __name__ == "__main__":
    main()
