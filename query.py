from socket import *
TCP_Client = socket(AF_INET, SOCK_STREAM) #tcp 소켓생성
TCP_Client.connect(('205.1.1.251', 9999)) #서버 IP와 포트번호 접속

data = bytearray([0x7E, 0x01, 0x01, 0xD1, 0x88])
TCP_Client.sendall(data) #보내고 싶은 데이터를 ""안에 입력 후 인코딩 후 전송 