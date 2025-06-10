# Relatório Técnico – Trabalho 1: Cliente-Servidor com Sockets em Python

Curso: Engenharia da Computação  
Disciplina: DEC7557 – Redes de Computadores  
Professora: Analucia Schiaffino Morales  
Dupla: Ludmila Silveira e Fernando Moretti
Data: 10/06/2025

## 1. Objetivo

Este trabalho teve como objetivo desenvolver uma aplicação cliente-servidor em Python utilizando sockets, implementando comunicação via UDP para simular o funcionamento do comando `ping`, com medição do tempo de ida e volta (RTT). Posteriormente, o programa foi adaptado para o protocolo TCP e executado entre duas máquinas diferentes na mesma rede local.

## 2. Metodologia

### 2.1 Ambiente de Testes

- Máquina Servidor:
  - IP: 200.135.80.189
  - SO: Windows 11
- Máquina Cliente:
  - IP: 200.135.76.7
  - SO: Windows 11
- Linguagem: Python 3
- Comunicação via rede local (Wi-Fi)
- Porta UDP: 22222
- Porta TCP: 22223

### 2.2 Implementação – UDP

O cliente envia 10 mensagens “ping” por UDP ao servidor. O servidor responde com a mesma mensagem, e o cliente mede o RTT. Um timeout de 1 segundo foi implementado para detectar perdas de pacotes.

### 2.3 Implementação – TCP

O servidor TCP escuta conexões e aceita uma conexão persistente do cliente, que envia as mesmas 10 mensagens, recebendo e medindo o RTT de cada resposta.

## 3. Resultados

### 3.1 Execuções Realizadas

Durante os testes entre duas máquinas reais, foram registrados os seguintes comportamentos:

- No UDP:
  - Mensagens recebidas corretamente
  - RTTs exibidos no terminal do cliente

- No TCP:
  - Conexão estabelecida com sucesso
  - Todas as mensagens recebidas corretamente

### 3.2 Capturas de Tela

Inserir aqui imagens dos terminais de execução:

- Cliente UDP:
- ![ClienteUDP](https://github.com/user-attachments/assets/52e8546a-a1cc-41e2-bdd9-45b930314574)
- Servidor UDP:  
- ![Servidor UDP](https://github.com/user-attachments/assets/a4f34f2e-4e1f-4606-b15a-f8502c567d00)
- Cliente TCP:  
- ![Cliente TCP](https://github.com/user-attachments/assets/f29854f5-be87-43a1-9e73-b942e92daaa0)
- Servidor TCP:
- ![Servidor TCP](https://github.com/user-attachments/assets/509418f5-8ab4-4861-8bf5-4c9aad11d11c)

## 4. Discussão

- A implementação com UDP exigiu a definição de um tempo limite (timeout) para detectar pacotes perdidos.
- A versão TCP foi mais simples quanto ao controle de confiabilidade, pois o protocolo já trata retransmissões e confirmações.
- A utilização de IPs reais da rede local foi essencial para a comunicação entre as máquinas.
- O teste com duas máquinas possibilitou uma experiência mais próxima do cenário real de redes.

## 5. Modificações Necessárias para Adaptar para TCP

As mudanças necessárias foram:

- Trocar socket.SOCK_DGRAM (UDP) por socket.SOCK_STREAM (TCP)
- No servidor:
  - Adicionar socket.listen() e socket.accept()
- No cliente:
  - Substituir sendto() e recvfrom() por sendall() e recv()
  - Usar socket.connect() para iniciar a conexão
- Remover necessidade de tratar endereço do remetente (endereco), pois o TCP gerencia a conexão

## 6. Conclusão

O trabalho proporcionou uma compreensão prática da utilização de sockets em Python com UDP e TCP. A experiência de rodar o programa em duas máquinas reais permitiu observar as diferenças práticas entre os protocolos de transporte e a importância da confiabilidade nas transmissões de dados.
