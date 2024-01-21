from typing import Iterator

def fibonacci_price_generator(n: int) -> Iterator[int]:
    fib1, fib2 = 0, 1
    while n + 1:
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1

price_sequence = fibonacci_price_generator(5)
print(price_sequence)