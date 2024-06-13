memo = {}

def fib(n: int) -> int:
    if n < 0:
        return None
    if n < 2:
        return n
    if n in memo:
        return memo[n]
    
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

# Example usage
print(fib(20))  # Output: 55
print(memo)

def fibonacci(n):
    for i in range(1, n + 1):
        if i <= 2:
            result = 1
        else:
            result = memo[i - 1] + memo[i - 2]
        memo[i] = result

    return memo[n]

print(fibonacci(20))
print(memo)