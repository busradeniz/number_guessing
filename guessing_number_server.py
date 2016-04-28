from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from random import randint


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/number-guessing-game',)


# Create server
server = SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler, logRequests=True)
server.register_introspection_functions()

lucky_number = randint(0, 100)


def guess(x):
    global lucky_number
    if x < lucky_number:
        return "bigger than this"
    elif x > lucky_number:
        return "less than this"
    elif x == lucky_number:
        lucky_number = randint(0, 100)
        return "correct!"


server.register_function(guess, 'guess')

try:
    print "Server is running... You can start guessing! (Use Control-C to exit)"
    server.serve_forever()
except KeyboardInterrupt:
    print '...Exiting...'
