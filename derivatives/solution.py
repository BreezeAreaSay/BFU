p, q, r = map(int, input().split())

f = (9 * p * q * r - 2 * q ** 3) / (27 * p * p)

print(f"{f:.12f}")
