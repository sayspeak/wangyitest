N, L = map(int, input().split())

parents = [int(i) for i in input().split()]

nodes_depth = [0] * N

for i in range(N - 2):
    nodes_depth[i + 1] = nodes_depth[parents[i]] + 1

max_depth = max(nodes_depth)

if L <= max_depth:
    max_cities = L + 1
else:
    max_cities = max_depth + ((L - max_depth) // 2) + 1

if max_cities <= N:
    print(max_cities)
else:
    print(N)