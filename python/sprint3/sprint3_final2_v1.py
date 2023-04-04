# 85130030


def partition(array, pivot):
    """Arrays comparation, item 1 -> item 2 -> item 0."""
    left = []
    center = []
    right = []
    for i in array:
        if i[1] > pivot[1]:
            left.append(i)
        elif i[1] < pivot[1]:
            right.append(i)
        else:
            if i[2] < pivot[2]:
                left.append(i)
            elif i[2] > pivot[2]:
                right.append(i)
            else:
                if i[0] < pivot[0]:
                    left.append(i)
                elif i[0] > pivot[0]:
                    right.append(i)
                else:
                    center.append(i)
    return left, center, right


def quicksort(array):
    """Quicksort with middle item as pivot."""
    if len(array) < 2:
        return array
    else:
        pivot = array[len(array) // 2]
        left, center, right = partition(array, pivot)
        return quicksort(left) + center + quicksort(right)


def read_input():
    n = int(input())
    arr = [None] * n
    for i in range(n):
        arr[i] = input().split()
        arr[i][1], arr[i][2] = int(arr[i][1]), int(arr[i][2])
    return arr


def main():
    result = quicksort(read_input())
    for i in result:
        print(i[0])


if __name__ == "__main__":
    main()
