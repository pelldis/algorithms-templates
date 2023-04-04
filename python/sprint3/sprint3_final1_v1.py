# 85109546


def broken_search(nums, target) -> int:
    """Lookup number in broken sequence."""
    start = 0
    end = len(nums) - 1

    while start <= end:
        k = (start + end) // 2
        if nums[k] == target:
            return k
        # if correct sequence
        if nums[start] <= nums[k]:
            if nums[k] > target >= nums[start]:
                end = k - 1
            else:
                start = k + 1
        # if broken sequence
        else:
            if nums[k] < target <= nums[end]:
                start = k + 1
            else:
                end = k - 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


def main():
    test()


if __name__ == "__main__":
    main()
