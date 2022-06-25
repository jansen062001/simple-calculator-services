from celery import Celery


prime_app = Celery('prime',
             broker='amqp://',
             backend='rpc://',
             include=['dependencies.prime'])
prime_app.conf.task_routes = {
    'dependencies.prime.get_prime': {'queue': 'prime'}
}

prime_palindrome_app = Celery('prime_palindrome',
             broker='amqp://',
             backend='rpc://',
             include=['dependencies.prime_palindrome'])
prime_palindrome_app.conf.task_routes = {
    'dependencies.prime_palindrome.get_prime_palindrome': {'queue': 'prime_palindrome'}
}
