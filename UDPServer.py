from socket import *


# 포트 번호
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

# 포트 번호를 서버의 소켓에 할당
# 서버 측에서는 명시적으로 포트 번호를 소켓에 할당해야 한다.
serverSocket.bind(('', serverPort))
print('The Server is ready to receive')

# 클라이언트로부터 계속해서 패킷을 수신하고 처리할 수 있도록 while 루프
while True:
    # 패킷이 서버의 소켓에 도착하면
    # 패킷의 데이터는 message 에 할당되고
    # 패킷의 소스 주소는 clientAddress 에 할당된다. (클라이언트의 IP 주소와 클라이언트의 포트 번호 포함)
    message, clientAddress = serverSocket.recvfrom(2048)

    # 대문자 변환
    modifiedMessage = message.decode().upper()

    # 클라이언트의 주소를 대문자로 변환한 메세지에 붙여 패킷으로 만들고 서버의 소켓으로 보낸다.
    # 인터넷이 패킷을 클라이언트 주소로 전달
    # 서버는 패킷을 보낸후 while 루프에 머무르면서 다른 UDP 패킷이 도착하기를 기다린다.
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
