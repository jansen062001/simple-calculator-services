from .celery import prime_app


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True


@prime_app.task
def get_prime(index):
    num = 1
    count_prime = 0
    
    while count_prime < index:
        num += 1
        
        if is_prime(num):
            count_prime += 1
    
    return num
