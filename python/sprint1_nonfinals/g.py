def to_binary(number: int) -> str:
    # Здесь реализация вашего решения
    if number == 0:
        return "0"
    lst = []
    while number >= 2:
        ost = number % 2
        number = int(number / 2)
        lst.append(str(ost))
    lst.append("1")
    return "".join(lst)[::-1]


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
