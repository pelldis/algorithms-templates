from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    # Здесь реализация вашего решения
    if len(temperatures) == 1:
        return 1
    result = 0
    start_step = 1
    end_step = len(temperatures) - 1
    if temperatures[0] > temperatures[1]:
        result += 1
        start_step += 1
    if temperatures[-1] > temperatures[-2]:
        result += 1
        end_step -= 1
    for i in range(start_step, end_step):
        if temperatures[i] > temperatures[i - 1] and temperatures[i] > temperatures[i + 1]:
            result += 1
    return result


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))
