## O objetivo desse projeto é criar uma aplicação cliente-servidor em Python, usando sockets, que:

* Usa UDP inicialmente;
* Mede o RTT (tempo de ida e volta) para cada pacote ping enviado;
* Envia 10 mensagens ping;
* Implementa timeout de 1 segundo (tratando perda de pacotes);
* Depois, será adaptada para TCP;

Tudo será executado em duas máquinas reais (ou virtuais), comunicando-se pela rede local (LAN) ou Wi-Fi.
