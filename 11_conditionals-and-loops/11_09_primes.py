# Print out every prime number between 1 and 1000.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for num in range(2, 1001):  
    if is_prime(num):
        print(num)