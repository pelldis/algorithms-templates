import sys


def is_correct_bracket_seq(scobes):
    scobe_types = {
        "{": "}",
        "[": "]",
        "(": ")"
    }
    if len(scobes) % 2 == 1:
        return False
    lst = []
    for i, scobe in enumerate(scobes):
        if not lst and scobe in "}])":
            return False
        if scobe in "{[(":
            lst.append(scobe_types[scobe])
        else:
            if lst[-1] == scobe:
                lst.pop()
            else:
                return False
    if not lst:
        return True
    return False


def read_input():
    """Read from input and make list with numbers."""
    return sys.stdin.readline().rstrip()


def main():
    print(is_correct_bracket_seq(read_input()))


if __name__ == "__main__":
    main()
