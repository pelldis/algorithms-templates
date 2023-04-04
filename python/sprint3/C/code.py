def solution(arr1, arr2):
    n = 0
    k = 0
    while n < len(arr2):
        check = False
        if arr1[k] == arr2[n]:
            k += 1
            check = True
        n += 1
        if k == len(arr1) and check:
            return True
    return False


def read_input():
    arr1 = input()
    arr2 = input()
    return arr1, arr2


def main():
    print(solution(*read_input()))


if __name__ == "__main__":
    main()
