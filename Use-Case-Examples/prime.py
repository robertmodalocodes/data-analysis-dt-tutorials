def prime_checker(number):
    if number % 1 == 0 and number % number == 0 and number % 2 != 0 and number % 3 != 0:
        print("It's a prime number")
    else:
        print("It's not a prime number")


n = int(input())
prime_checker(number=n)

# Angela's code


def prime_checker_2(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
