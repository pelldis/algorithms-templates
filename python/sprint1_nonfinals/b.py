def check_parity(a: int, b: int, c: int) -> bool:
    # Здесь реализация вашего решения
    if a % 2 == b % 2 and a % 2 == c % 2:
        return True
    return False


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
