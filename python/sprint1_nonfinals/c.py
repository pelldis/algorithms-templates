from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    # Здесь реализация вашего решения
    n1 = [row, col - 1]
    n2 = [row - 1, col]
    n3 = [row + 1, col]
    n4 = [row, col + 1]
    result = []
    for i, j in [n1, n2, n3, n4]:
        if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
            result.append(matrix[i][j])
    result.sort()
    return result


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col


matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
