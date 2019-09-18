import zerorpc

# Inisisi class
class Hello(object):
    # Buat remote function yang harus dieksekusi oleh server
    # - Nama fungsi : hello
    # - Parameter : data berupa string
    def hello(self, data):
        return "Hello, %s" % data
    
    def jumlah(self, a, b):
        return (a+b)

# Inisiasi server
server = zerorpc.Server(Hello())
# Binding ke IP dan port tertentu
server.bind("tcp://0.0.0.0:8888")
server.run()