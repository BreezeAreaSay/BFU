n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

moves = 0
balance = 0
for i in range(n):
    diff = b[i] - a[i]
    balance += diff
    if diff > 0:
        moves += diff

print(moves if balance == 0 else -1)
