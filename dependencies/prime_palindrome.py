from .celery import prime_palindrome_app


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True


def is_palindrome(s):
    return s == s[::-1]


@prime_palindrome_app.task
def get_prime_palindrome(index):
    num = 1
    count_prime_palindrome = 0
    
    while count_prime_palindrome < index:
        num += 1
        
        if is_prime(num) and is_palindrome(str(num)):
            count_prime_palindrome += 1
    
    return num
