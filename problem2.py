#problem: write a function to calculate a factorial of a number
def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

number = 5
try:
    fact_result = factorial(number)
    print(f"The factorial of {number} ({number}!) is {fact_result}")
    print(f"The factorial of 0 (0!) is {factorial(0)}")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
