import socket

IP = '200.135.80.184'
PORTA = 12001

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((IP, PORTA))
servidor.listen(1)

print(f"Servidor TCP escutando em {IP}:{PORTA}...")
conn, addr = servidor.accept()
print(f"Conectado com {addr}")

for _ in range(10):
    dados = conn.recv(1024)
    print(f"Recebido: {dados.decode()}")
    conn.sendall(dados)

conn.close()
