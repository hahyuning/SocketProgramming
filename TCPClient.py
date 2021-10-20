from socket import *

# IP 주소 또는 호스트 이름
# 호스트 이름을 사용하는 경우 IP 주소를 얻기 위해 DNS 검색 자동 수행
serverName = ''
# 포트 번호
serverPort = 12000

# 클라이언트의 소켓 생성
# 첫번째 파라미터: 주소군 (AF_INET - IPv4)
# 두번째 파라미터: 소켓 종류 (SOCK_STREAM - TCP 소켓)
# 소켓을 생성할 때 클라이언트 소켓의 포트 번호를 명시하지 않아도 되며 운영체제가 이 작업을 대신 수행
clientSocket = socket(AF_INET, SOCK_STREAM)

# 클라이언트가 TCP 소켓을 이용하여 서버로 데이터를 보내기 전에 TCP 연결이 설정되어야 한다.
# connect(서버쪽 주소): 이 메서드가 실행되면 세 방향 핸드셰이크가 수행되고 TCP 연결이 설정된다.
clientSocket.connect((serverName, serverPort))

# 서버에 보낼 메세지 생성
sentence = input('Input lowercase sentence:')

# encode(): 바이트 형태로 보내기 위해 문자열 타입의 메시지를 바이트 타입으로 변환
# send(): 클라이언트의 소켓을 통해 TCP 연결로 보낸다.
# UDP 소켓처럼 패킷을 명시적으로 생성하지 않으며 패킷에 목적지 주소를 붙이지 않는다.
# 클라이언트 프로그램은 단순히 문자열에 있는 바이트를 TCP 연결에게 제공
clientSocket.send(sentence.encode())

# 서버로부터 온 문자를 modifiedMessage 에 할당
modifiedMessage = clientSocket.recv(1024) # 버퍼크기 설정

# 메시지를 바이트에서 문자열로 변환한다음 화면에 출력
print(modifiedMessage.decode())

# 소켓을 닫고 TCP 연결을 닫는다.
clientSocket.close()