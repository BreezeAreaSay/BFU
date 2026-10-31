import subprocess
import sys
from pathlib import Path

SOLUTION = Path(__file__).with_name("solution.py")

N_MAX = 100
BIG = 10 ** 6
A_MAX = " ".join("1" if i % 2 == 0 else str(BIG) for i in range(N_MAX))
B_MAX = " ".join(str(BIG) if i % 2 == 0 else "1" for i in range(N_MAX))

# (входные данные, правильный ответ)
TESTS = [
    ("1\n1000000\n999999\n", "-1"),  # пример 1 из условия
    ("3\n1 2 3\n3 2 1\n", "2"),  # пример 2 из условия
    ("3\n5 5 5\n5 5 5\n", "0"),  # наборы уже совпадают
    ("1\n7\n7\n", "0"),  # одна башня
    ("4\n1 1 1 10\n4 4 4 1\n", "9"),  # лишние кубики в нескольких башнях
    ("2\n3 4\n3 5\n", "-1"),  # суммы различаются
    (f"{N_MAX}\n{A_MAX}\n{B_MAX}\n", "49999950"),  # максимальный тест
]


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
        elif got.split() == expected.split():
            verdict = "OK"
        else:
            verdict = "WA"
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
