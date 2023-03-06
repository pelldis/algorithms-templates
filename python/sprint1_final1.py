from typing import List, Tuple


def nearest_zero(number_list, count) -> List[int]:
    new_lst = [0] * count
    step = 0
    for i, number in enumerate(number_list):
        if number == 0:
            new_lst[i] = number
            step = 0
        else:
            step += 1
            new_lst[i] = step
    new_lst2 = []
    step = 0
    start_trigger = False
    end_trigger = False
    if number_list[0] == 0:
        end_trigger = True
    zero_count = [0] * number_list.count(0)
    for i, number in enumerate(reversed(new_lst)):
        if number == 0:
            new_lst2.append(number)
            step = 0
            start_trigger = True
            zero_count.pop()
        else:
            step += 1
            if (end_trigger or zero_count) and start_trigger:
                if step < new_lst[-i - 1]:
                    new_lst2.append(step)
                else:
                    new_lst2.append(new_lst[-i - 1])
            elif not zero_count:
                new_lst2.append(step)
            else:
                new_lst2.append(new_lst[-i - 1])
    return list(reversed(new_lst2))


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    return number_list, n


def main():
    number_list, count = read_input()
    print(*nearest_zero(number_list, count))


if __name__ == "__main__":
    main()
