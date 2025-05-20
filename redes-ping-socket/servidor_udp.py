import socket

IP = '200.135.80.184'  # IP da máquina servidor
PORTA = 12000

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind((IP, PORTA))

print(f"Servidor UDP aguardando pings em {IP}:{PORTA}...")

while True:
    mensagem, endereco = servidor.recvfrom(1024)
    print(f"Recebido de {endereco}: {mensagem.decode()}")
    servidor.sendto(mensagem, endereco)