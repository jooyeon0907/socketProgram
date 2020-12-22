from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)

host = "172.16.3.101"
port = 8080
clientSock.connect((host, port)) 
# 서버소켓에서 사용한 bind, listen, accept 과정이 빠지고 connect가 추가됨.
# 클라이언트에서 서버에 접속하기 위해 connect() 실행.
# connect() 에 어드레스 패밀리(AF)가 인자로 들어가고, 호스트와 포트 번호 번호로 구성된 튜플이 요구됨
# host -> 연결할 서버 IP 주소, port -> 열린 포트로 연결

# 172.0.0.1은 자기 자신을 의미. (로컬로 test용)-> 자기 자신에게 8080번 포트로 연결하기


print('client >>  연결 확인이 되었습니다.')
"""
clientSock.send('I am a client'.encode('utf-8'))

print('client >> 메시지를 전송완료.')

data = clientSock.recv(1024)
print('client >>  받은 데이터 :', data.decode('utf-8'))
"""

while True:
    recvData = clientSock.recv(1024)
    if recvData.decode('utf-8') == "":
        break
    print('상대방(server) : ',recvData.decode('utf-8'))

    sendData = input('client >>> ')

    clientSock.send(sendData.encode('utf-8'))

clientSock.close()
print('clientSock Close')