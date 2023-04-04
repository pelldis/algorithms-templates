def solution(array, price, left, right):
    if right <= left:
        if max(array) < price:
            return -1
        return left + 1
    mid = (left + right) // 2
    if array[mid] == price:
        return array.index(price) + 1
    elif price < array[mid]:
        return solution(array, price, left, mid)
    else:
        return solution(array, price, mid + 1, right)


def read_input():
    input()
    array = list(map(int, input().split()))
    bike_price = int(input())
    return bike_price, array


def main():
    price, array = read_input()
    x1 = solution(array, price, 0, len(array))
    x2 = solution(array, price * 2, 0, len(array))
    print(x1, x2)


if __name__ == "__main__":
    main()
