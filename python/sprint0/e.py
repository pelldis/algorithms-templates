from typing import List, Tuple, Optional


# def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
#    # Здесь реализация вашего решения
#    left = 0
#    right = len(arr) - 1
#    arr.sort()
#    while left < right:
#        cur_sum = arr[left] + arr[right]
#        if cur_sum == target_sum:
#            return arr[left], arr[right]
#        if cur_sum > target_sum:
#            right -= 1
#        else:
#            left += 1
#    return None
#
def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    numbers = set()
    for x in arr:
        y = target_sum - x
        if y in numbers:
            return y, x
        else:
            numbers.add(x)
    return None

def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))


arr, target_sum = read_input()
print_result(two_sum(arr, target_sum))
