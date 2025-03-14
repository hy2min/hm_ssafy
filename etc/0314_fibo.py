def fibo(n):
    if memo[n] != -1:
        return memo[n]

    if n <= 1:
        return

    memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

memo = [-1] * 5
memo[0] = 0
memo[1] = 1

fibo(4)
print(*memo)