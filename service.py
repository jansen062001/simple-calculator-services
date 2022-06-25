from unittest import result
from nameko.rpc import rpc
from dependencies.prime import get_prime, prime_app
from dependencies.prime_palindrome import prime_palindrome_app, get_prime_palindrome
from celery.result import AsyncResult


class CalculatorService:
    name = 'calculator_service'
    
    @rpc
    def get_prime(self, index):
        if index <= 0:
            return {
                'response_code': 404,
                'response_data': {
                    "status": "error",
                    "message": "Not found"
                }
            }
        else:
            id = get_prime.apply_async([index])
            result = AsyncResult(id.id, app=prime_app)
            
            return {
                'response_code': 200,
                'response_data': {
                    "result": result.get()
                }
            }
    
    
    @rpc
    def get_prime_palindrome(self, index):
        if index <= 0:
            return {
                'response_code': 404,
                'response_data': {
                    "status": "error",
                    "message": "Not found"
                }
            }
        else:
            id = get_prime_palindrome.apply_async([index])
            result = AsyncResult(id.id, app=prime_palindrome_app)
            
            return {
                'response_code': 200,
                'response_data': {
                    "result": result.get()
                }
            }
