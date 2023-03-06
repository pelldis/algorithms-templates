from typing import List, Tuple


def calculate_score(number_list, n) -> int:
    """Calculate score from list with numbers."""
    result = 0
    for i in set(number_list):
        if n * 2 >= number_list.count(i):
            result += 1
    return result


def read_input() -> Tuple[List[int], int]:
    """Read from input and make list with numbers."""
    n = int(input())
    number_list = []
    for _ in range(4):
        number_list += list(input().strip())
    number_list = [int(i) for i in number_list if i != "."]
    return number_list, n


def main():
    number_list, count = read_input()
    print(calculate_score(number_list, count))


if __name__ == "__main__":
    main()
