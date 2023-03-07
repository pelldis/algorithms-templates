from typing import List, Tuple
# ID 83489400


def calculate_score(number_list, n) -> int:
    """Calculate score from list with numbers."""
    result = 0
    # iterate uniq numbers in list using set
    # add one point if count of numbers < or = (n * 2)
    for i in set(number_list):
        if n * 2 >= number_list.count(i):
            result += 1
    return result


def read_input() -> Tuple[List[int], int]:
    """Read from input and make list with numbers."""
    n = int(input())
    number_list = []
    # read string from input and make one list
    for _ in range(4):
        number_list += list(input().strip())
    # remove . from list and move numbers from string to int
    number_list = [int(i) for i in number_list if i != "."]
    return number_list, n


def main():
    number_list, count = read_input()
    print(calculate_score(number_list, count))


if __name__ == "__main__":
    main()
