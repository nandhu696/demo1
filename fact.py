def factorial(n):
    if n < 0:
        return None

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", n, "is", factorial(n))
#End of the program
