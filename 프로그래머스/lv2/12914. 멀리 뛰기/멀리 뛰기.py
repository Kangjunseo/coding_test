from itertools import product

def solution(n):
    answer = 0
    dp = [1] + [0] * n
    dp[0], dp[1] = 1, 1
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    return dp[n]