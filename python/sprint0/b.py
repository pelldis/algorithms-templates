from typing import List, Tuple


def zipper(a: List[int], b: List[int]) -> List[int]:
    # Здесь реализация вашего решения
    c, d = list(zip(a, b)), []
    [d.extend(list(i)) for i in c]
    return d


def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b


a, b = read_input()
print(" ".join(map(str, zipper(a, b))))
