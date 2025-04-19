n, t = map(int, input().split())
time = list(map(int, input().split()))
l = 0
total = 0
count = 0

for i in range(n):
    total += time[i]
    while total > t:
        total -= time[l]
        l += 1
    count = max(count, i - l + 1)

print(count)
