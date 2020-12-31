N, M = map(int, input().split())
helmets = list(map(int, input().split()))
chokkis = list(map(int, input().split()))

print(max(helmets) + max(chokkis))