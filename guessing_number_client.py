import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000/number-guessing-game')

result = ''
try:
    while result != 'correct!':
        guess = input('Please guess a number between 0 and 100: ')
        result = s.guess(guess)
        print result
except KeyboardInterrupt:
    print '...Exiting...'
