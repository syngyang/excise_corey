import sys
import requests

print(sys.version)
print(sys.executable)

def greet(who_to_greet):
    greeting = 'Hello,{}'.format(who_to_greet)
    return greeting

# print(greet('syng'))
# print(greet('Yang'))

r = requests.get('http://www.4ok.kr')
print(r.status_code)

# name = input("Your name? ")
# print('Hello, {}'.format(name))
