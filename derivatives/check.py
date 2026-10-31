import subprocess
import sys
from pathlib import Path

SOLUTION = Path(__file__).with_name("solution.py")
EPS = 1e-6

# (входные данные, правильный ответ)
TESTS = [
    ("8 24 100\n", 84),  # пример из условия
    ("8 -24 -68\n", 84),  # a = -2, b = 4, c = 21
    ("2 3 3\n", 1),  # a = 1, b = 1, c = 1
    ("2 -6 14\n", -10),  # a = 1, b = -2, c = 5
    ("2 0 0\n", 0),  # a = 1, b = 0, c = 0
    ("1000 0 -1000\n", 0),  # b = 0, значит f = 0
    ("1 1 1\n", 7 / 27),  # нецелый ответ
    ("1000 1000 1000\n", 7000 / 27),  # максимальные p, q, r
    ("1 -1000 -1000\n", 2009000000 / 27),  # большой ответ
    ("1 1000 -1000\n", -2009000000 / 27),  # большой отрицательный ответ
]


def is_close(got, expected):
    return abs(got - expected) <= EPS * max(1, abs(expected))


def main():
    failed = 0
    for number, (test_input, expected) in enumerate(TESTS, 1):
        result = subprocess.run(
            [sys.executable, str(SOLUTION)],
            input=test_input,
            capture_output=True,
            text=True,
        )
        got = result.stdout.strip()
        if result.returncode != 0:
            verdict = "RE"
        else:
            try:
                verdict = "OK" if is_close(float(got), expected) else "WA"
            except ValueError:
                verdict = "PE"
        print(f"Тест {number}: {verdict}")
        if verdict != "OK":
            failed += 1
            print(f"  ожидалось: {expected}")
            print(f"  получено:  {got}")
            print(result.stderr, end="")
    if failed:
        print(f"Не пройдено тестов: {failed} из {len(TESTS)}")
        sys.exit(1)
    print("Все тесты пройдены")


if __name__ == "__main__":
    main()
