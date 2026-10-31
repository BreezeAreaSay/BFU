import sys


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:n + 1]))
    b = list(map(int, data[n + 1:2 * n + 1]))

    if sum(a) != sum(b):
        print(-1)
    else:
        print(sum(bi - ai for ai, bi in zip(a, b) if bi > ai))


if __name__ == "__main__":
    main()
