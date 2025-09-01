def sum_of_natural_numbers(n):
    return n * (n + 1) // 2
n = int(input("Enter a positive integer: "))
print(f"The sum of the first {n} natural numbers is {sum_of_natural_numbers(n)}")
