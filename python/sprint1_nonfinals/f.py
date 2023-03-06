import re


def is_palindrome(line: str) -> bool:
    # Здесь реализация вашего решения
    line = re.split(': |, | |\.', line)
    line = "".join(line).lower()
    if len(line) % 2 == 0:
        first_part = line[0:int(len(line) / 2)]
        last_part = line[:(int(len(line) / 2) - 1):-1]
        if first_part == last_part:
            return True
    else:
        first_part = line[0:int(len(line) / 2)]
        last_part = line[:int(len(line) / 2):-1]
        if first_part == last_part:
            return True
    return False


print(is_palindrome(input().strip()))
