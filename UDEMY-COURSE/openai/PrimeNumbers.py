# Initialize a list to store the prime numbers
primes = []

# Loop through all the numbers from 2 to 1000
for num in range(2, 1001):
    # Assume that the number is prime
    is_prime = True

    # Check if the number is prime
    for i in range(2, num):
        if num % i == 0:
            # If the number is evenly divisible by any number between 2 and itself, it is not prime
            is_prime = False
            break

    # If the number is prime, add it to the list of prime numbers
    if is_prime:
        primes.append(num)

# Print the list of prime numbers
print(primes)
