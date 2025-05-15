import sys

# Number of cities
n = 4

# Distance matrix (symmetric, 0 means same city)
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Memoization table
dp = [[-1] * n for _ in range(1 << n)]

def tsp(mask, pos):
    if mask == (1 << n) - 1:  # all cities visited
        return dist[pos][0]  # return to starting city

    if dp[mask][pos] != -1:
        return dp[mask][pos]

    min_cost = sys.maxsize
    for city in range(n):
        if (mask >> city) & 1 == 0:  # if not visited
            new_cost = dist[pos][city] + tsp(mask | (1 << city), city)
            min_cost = min(min_cost, new_cost)

    dp[mask][pos] = min_cost
    return min_cost

# Start from city 0 with only city 0 visited (bitmask 0001)
result = tsp(1, 0)
print("Minimum cost to visit all cities:", result)
