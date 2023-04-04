def solution(n, scobe_open, scobe_close, prefix):
    if scobe_open + scobe_close == 2 * n:
        print(prefix)
        return
    if scobe_open < n:
        solution(n, scobe_open + 1, scobe_close, prefix + '0')
    if scobe_open > scobe_close:
        solution(n, scobe_open, scobe_close + 1, prefix + '1')


def read_input():
    return int(input())


def main():
    solution(read_input(), 0, 0, "")


if __name__ == "__main__":
    main()
