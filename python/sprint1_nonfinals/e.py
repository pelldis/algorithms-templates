def get_longest_word(line: str) -> str:
    # Здесь реализация вашего решения
    line = line.split()
    max_length = 0
    result = ""
    for word in line:
        if len(word) > max_length:
            max_length = len(word)
            result = word
    return result


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
