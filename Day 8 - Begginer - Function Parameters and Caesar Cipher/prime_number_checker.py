def prime_number_cheker(number):
    is_prime = True
    for i in range(2, number - 1):
        if number % i == 0:
            is_prime = False
        if is_prime:
            print("It's a prime number.")
        else:
            print(f"It's number {number} not a prime number")