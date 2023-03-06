from typing import List, Tuple

def get_sum(number_list: List[int], k: int) -> List[int]:
    # Здесь реализация вашего решения
    number_list = [str(i) for i in number_list]
    x = "".join(number_list)
    return list(str(int(x) + k))

def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k

number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))
