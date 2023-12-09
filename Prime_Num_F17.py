def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_div = int(n**0.5) + 1
    for i in range(3, max_div, 2):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
if is_prime(n):
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")