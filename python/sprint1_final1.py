from typing import List, Tuple
# ID 83488463


def nearest_zero(number_list, count) -> List[int]:
    """Calculate the shortest distance to zero."""
    # create list with count "count" zeros
    new_lst = [0] * count
    step = 0
    # first iterate and fill new_list with zeros and distance
    for i, number in enumerate(number_list):
        if number == 0:
            new_lst[i] = number
            # reset step to zero if number = 0
            step = 0
        else:
            # calculate distance after beginning of list or zero
            step += 1
            new_lst[i] = step
    # create lst2 for fill final result during reverse iterate new_lst
    new_lst2 = []
    step = 0
    start_trigger = False
    end_trigger = False
    # if base number list starts with zero set trigger to True
    # now we know that reverse iteration ends with zero
    if number_list[0] == 0:
        end_trigger = True
    # create list with a number of zeros in base number list
    zero_count = [0] * number_list.count(0)
    # reverse iteration for comparison distance to zero and set smaller
    for i, number in enumerate(reversed(new_lst)):
        if number == 0:
            new_lst2.append(number)
            # reset step to zero if number = 0
            step = 0
            # set trigger that next section starts with zero and
            # remove one zero from list of zeros
            start_trigger = True
            zero_count.pop()
        else:
            step += 1
            # if section starts with zero and ends with zero
            if (end_trigger or zero_count) and start_trigger:
                if step < new_lst[-i - 1]:
                    new_lst2.append(step)
                else:
                    new_lst2.append(new_lst[-i - 1])
            # if section ends with not zero
            elif not zero_count:
                new_lst2.append(step)
            # if section starts with not zero
            else:
                new_lst2.append(new_lst[-i - 1])
    return list(reversed(new_lst2))


def read_input() -> Tuple[List[int], int]:
    """Read number and list of numbers."""
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    return number_list, n


def main():
    number_list, count = read_input()
    print(*nearest_zero(number_list, count))


if __name__ == "__main__":
    main()
