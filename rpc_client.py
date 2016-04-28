import xmlrpclib
from random import randint

#select and print two number randomly
first_lucky_number = randint(0, 100000)
print 'first lucky number :', first_lucky_number
second_lucky_number = randint(0, 100000)
print 'second lucky number :', second_lucky_number


#connect to server
server = xmlrpclib.Server('http://www.advogato.org/XMLRPC')

#call sumprod function of server
(sum, prod) = server.test.sumprod(first_lucky_number, second_lucky_number)

#print sum and prod results
print 'sum :', sum
print 'prod :',prod
