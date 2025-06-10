import socket
import time

SERVER_IP = '200.135.80.38'  # IP da máquina servidor
SERVER_PORT = 22222

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente.settimeout(10)  # timeout de 1 segundo

for i in range(1, 11):
    mensagem = f"Ping {i} {time.time()}"
    try:
        tempo_inicio = time.time()
        cliente.sendto(mensagem.encode(), (SERVER_IP, SERVER_PORT))

        resposta, _ = cliente.recvfrom(1024)
        tempo_fim = time.time()

        rtt = tempo_fim - tempo_inicio
        print(f"Resposta {i}: {resposta.decode()} - RTT = {rtt:.4f} segundos")

    except socket.timeout:
        print(f"Resposta {i}: Tempo esgotado (pacote perdido)")
