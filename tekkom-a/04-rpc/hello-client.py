import zerorpc

# Inisiasi client
client = zerorpc.Client()
# Buat koneksi TCP ke server
client.connect("tcp://127.0.0.1:8888")
# Panggil remote function dengan nama "hello" dengan parameter berupa string
# - Client stub akan building message
# - Message akan dikirimkan ke server
# - Menerima response dari server
data = client.hello("Pagi")
# Cetak datanya
print(data)

data = client.jumlah(20,10)
print(data)