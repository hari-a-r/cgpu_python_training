def primes_in_interval(start, end):
    primes = []
    for num in range(start, end + 1):  # Iterate through numbers in the range
        if num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)  # Add prime numbers to the list
    return primes


start = int(input("Enter the starting value of the range: "))
end = int(input("Enter the ending value of the range: "))


if start > end:
    print("Invalid range! Starting value should be less than or equal to the ending value.")
else:

    print(f"Prime numbers between {start} and {end}:", primes_in_interval(start, end))
