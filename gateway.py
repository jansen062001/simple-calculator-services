# from fileinput import filename
import json
# from unittest import result
# from grpc import Status
# from matplotlib.font_manager import json_dump
from nameko.rpc import RpcProxy
from nameko.web.handlers import http
# from requests import session
from werkzeug.wrappers import Response
import os
# from flask import Flask, flash, request, redirect, url_for, send_from_directory, current_app
from flask import Flask, send_from_directory
from werkzeug.utils import secure_filename
import datetime


class CalculatorGatewayService:
    name = 'calculator_gateway'
    calculator_rpc = RpcProxy('calculator_service')
    
    @http('GET', '/api/prime/<int:index>')
    def get_prime(self, request, index):
        prime = self.calculator_rpc.get_prime(index)
        
        return int(prime['response_code']), json.dumps(prime['response_data'])
    
    
    @http('GET', '/api/prime/palindrome/<int:index>')
    def get_prime_palindrome(self, request, index):
        prime_palindrome = self.calculator_rpc.get_prime_palindrome(index)
        
        return int(prime_palindrome['response_code']), json.dumps(prime_palindrome['response_data'])
        