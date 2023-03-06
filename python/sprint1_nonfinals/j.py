from typing import List
from math import sqrt


def get_least_primes_linear(n):
    n = int(sqrt(n))
    numbers = list(range(n+1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(num * num, n + 1, num):
                numbers[j] = False
    numbers = [i for i in numbers if i]
    return numbers


def factorize(number: int) -> List[int]:
    # Здесь реализация вашего решения
    simple_digits = get_least_primes_linear(number)
    n = []
    numbers = [number]
    while number != 1:
        result = False
        for i in simple_digits:
            if number % i == 0:
                result = True
                n.append(i)
                numbers.append(int(number/i))
                number = int(number/i)
        if not result:
            number = 1
            n.append(numbers[-1])
    n.sort()
    return n


result = factorize(int(input()))
print(" ".join(map(str, result)))
