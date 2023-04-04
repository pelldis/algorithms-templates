def uniq_lists(a, b):
    return a[1] < b[0] or b[1] < a[0]


def merge(a, b):
    lst = []
    if a[0] <= b[0]:
        lst.append(a[0])
    else:
        lst.append(b[0])
    if a[1] >= b[1]:
        lst.append(a[1])
    else:
        lst.append(b[1])
    return lst


def insertion_sort(arr):
    n = 0
    lst = arr[0]
    while n < len(arr):
        if lst == arr[n]:
            lst = arr[n]
        else:
            if uniq_lists(lst, arr[n]):
                print(*lst)
                lst = arr[n]
            else:
                if lst[1] < arr[n][1]:
                    lst[1] = arr[n][1]
        n += 1
    print(*lst)


def read_input():
    n = int(input())
    arr = [None] * n
    for i in range(n):
        arr[i] = list(map(int, input().split()))
    return arr


def main():
    a = read_input().sort
    a.sort()
    insertion_sort(a)


if __name__ == "__main__":
    main()
