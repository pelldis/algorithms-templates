from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    # Здесь реализация вашего решения
    first = list(reversed(first_number))
    second = list(reversed(second_number))
    if len(first_number) >= len(second_number):
        second += [0] * (len(first) - len(second))
    else:
        first += [0] * (len(second) - len(first))
    sum = [0] * len(first)

    for i in range(len(second)):
        current_sum = int(first[i]) + int(second[i]) + sum[i]
        sum[i] = current_sum
        if current_sum == 2:
            sum[i] = 0
            if len(sum) > i + 1:
                sum[i + 1] += 1
            else:
                sum.append(1)
        elif current_sum == 3:
            sum[i] = 1
            if len(sum) > i + 1:
                sum[i + 1] += 1
            else:
                sum.append(1)
    sum = [str(i) for i in sum]
    return "".join(sum)[::-1]


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
