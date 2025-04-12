n, m = map(int, input().split())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
container = []

i = 0
j = 0
for k in range(n + m):
    if i < n and (j >= m or first[i] <= second[j]):
        container.append(first[i])
        i += 1
    else:
        container.append(second[j])
        j += 1

print(*container)
