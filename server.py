import xmlrpclib
from nextdate import nextdate, Date_my
from SimpleXMLRPCServer import SimpleXMLRPCServer

def nextdate_server(year, month, day):
	return nextdate(Date_my(year, month, day))

server = SimpleXMLRPCServer(("localhost", 8000))
print "Listening on port 8000..."
server.register_function(nextdate_server, "nextdate")
server.serve_forever()
