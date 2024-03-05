def is_prime(num):
    if num <= 1:
        print(num, "is not a prime number")
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number")
            return False
    
    print(num, "is a prime number")
    return True

num = 18
is_prime(num)
