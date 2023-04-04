def str_greater(a, b):
    return str(a) + str(b) > str(b) + str(a)


def solution(arr, n):
    for i in range(1, len(arr)):
        item_to_insert = arr[i]
        j = i
        while j > 0 and str_greater(item_to_insert, arr[j - 1]):
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = item_to_insert
    print("".join([str(i) for i in arr]))
    return arr


def read_input():
    n = int(input())
    arr = list(map(int, input().split()))
    return arr, n


def main():
    solution(*read_input())


if __name__ == "__main__":
    main()
