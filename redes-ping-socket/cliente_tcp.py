import socket
import time

SERVER_IP = '200.135.80.184'
SERVER_PORT = 12001

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((SERVER_IP, SERVER_PORT))

for i in range(1, 11):
    mensagem = f"Ping {i} {time.time()}"
    tempo_inicio = time.time()
    cliente.sendall(mensagem.encode())

    resposta = cliente.recv(1024)
    tempo_fim = time.time()

    rtt = tempo_fim - tempo_inicio
    print(f"Resposta {i}: {resposta.decode()} - RTT = {rtt:.4f} segundos")

cliente.close()
