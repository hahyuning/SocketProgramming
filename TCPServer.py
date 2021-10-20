from socket import *


# 포트 번호
serverPort = 12000
# 환영 소켓
serverSocket = socket(AF_INET, SOCK_STREAM)

# 포트 번호를 서버의 소켓에 할당
# 서버 측에서는 명시적으로 포트 번호를 소켓에 할당해야 한다.
serverSocket.bind(('', serverPort))

# 서버가 클라이언트로부터 TCP 연결 요청을 듣도록 한다.
# 파라미터: 큐되는 연결의 최대 수
serverSocket.listen(1)
print('The Server is ready to receive')

# 클라이언트로부터 계속해서 패킷을 수신하고 처리할 수 있도록 while 루프
while True:
    # 클라이언트가 문을 두드리면 프로그램은 accept() 메소드를 시작해서
    # 클라이언트에게 지정된 연결소켓이라는 새로운 소켓을 서버에 생성
    # 그 뒤 클라이언트와 서버는 핸드셰이킹을 완료해서 클라이언트 소켓과 서버의 연결 소켓 간에
    # TCP 연결을 생성한다.
    connectionSocket, addr = serverSocket.accept()

    # TCP 연결이 설정되면 클라이언트와 서버는 이 연결을 통해 서로에게 바이트 스트림을 보낼 수 있다.
    # TCP의 경우 한쪽에서 보낸 모든 바이트가 다른 쪽에 도착하는 것을 보장할 뿐만 아니라
    # 순서대로 도착하는 것을 보장한다.
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())

    # 클라이언트에게 수정된 문장을 보낸 후 연결 소켓을 닫는다.
    # 환영 소켓은 열려 있기 때문에 다른 클라이언트가 서버에게 문장을 보낼 수 있다.
    connectionSocket.close()

