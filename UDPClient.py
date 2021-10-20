from socket import *

# IP 주소 또는 호스트 이름
# 호스트 이름을 사용하는 경우 IP 주소를 얻기 위해 DNS 검색 자동 수행
serverName = ''
# 포트 번호
serverPort = 12000

# 클라이언트의 소켓 생성
# 첫번째 파라미터: 주소군 (AF_INET - IPv4)
# 두번째 파라미터: 소켓 종류 (SOCK_DGRAM - UDP 소켓)
# 소켓을 생성할 때 클라이언트 소켓의 포트 번호를 명시하지 않아도 되며 운영체제가 이 작업을 대신 수행
clientSocket = socket(AF_INET, SOCK_DGRAM)

# 서버에 보낼 메세지 생성
message = input('Input lowercase sentence:')

# encode(): 바이트 형태로 보내기 위해 문자열 타입의 메시지를 바이트 타입으로 변환
# sendto(): 목적지 주소를 메시지에 붙이고 그 패킷을 프로세스의 소켓인 clientSocket 으로 보낸다.
clientSocket.sendto(message.encode(), (serverName, serverPort))

# 패킷이 클라이언트의 소켓에 인터넷으로부터 도착하면
# 패킷 데이터는 modifiedMessage 에 할당되고
# 패킷의 소스 주소는 변수 serverAddress 에 할당된다. (서버의 IP 주소와 서버의 포트 번호 포함)
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) # 버퍼크기 설정

# 메시지를 바이트에서 문자열로 변환한다음 화면에 출력
print(modifiedMessage.decode())

# 소켓을 닫고 프로세스 종료
clientSocket.close()

