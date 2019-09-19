# Import library zerorpc
import zerorpc
# Inisiasi client
client = zerorpc.Client()
# Buat koneksi tcp ke server
client.connect("tcp://127.0.0.1:8888")
# Panggil remote procedure bernama "hello" dengan satu parameter string
data = client.hello("Tes")
# Print response
print(data)
data = client.jumlah(20,30)
print(data)