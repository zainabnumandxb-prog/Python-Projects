def fibonacci(n:int):
    sequence = [0, 1]

    if n == 0 or n == 1:
        return sequence[n]

    for i in range(2, n+1):
        next_val = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_val)

    return sequence[n]

print(fibonacci(0))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(10))
print(fibonacci(15))