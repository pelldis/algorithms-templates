from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    # Здесь реализация вашего решения
    shorter = sorted(shorter)
    longer = sorted(longer)
    for i in range(len(shorter)):
        if longer[i] != shorter[i]:
            return longer[i]
    return longer[-1]


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
