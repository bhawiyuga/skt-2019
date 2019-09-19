# Import library zerorpc
import zerorpc

# Inisiasi class
class Hello(object):
    # Inisiasi method hello yang nanti akan dipanggil oleh client
    def hello(self, data):
        return "Hello "+data
    def jumlah(self, a, b):
        return (a+b)

# Inisiasi server
server = zerorpc.Server(Hello())
# Binding
server.bind("tcp://0.0.0.0:8888")
# Running server
server.run()