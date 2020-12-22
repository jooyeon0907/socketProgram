from socket import *  # 기본 모듈 socket 불러옴 

## 서버 소켓 세팅 

serverSock = socket(AF_INET, SOCK_STREAM)  # 불러온 모듈(socket)로 소켓 생성하기 
# socket 객체를 생성. 두가지 인자 입력 받기 (AF 어드레스 패밀리 , 소켓타입)
# 어드레스 패밀리(Address Family) : 주소 체계에 해당 
# -> AF_INET : IP로 구성된 AF. IPv4를 의미 (AF_INET은 IPv6을 의미) 대부분 AF_INET 사용. 
# 소켓 타입: SOCK_STREAM(TCP), SOCK_DGRAM(UDP) 주로 사용됨

port =8080
serverSock.bind(('',port))
# 생성한 소켓을 bind 해주어야 됨 (클라이언트를 만들 때는 불필요하며, 서버를 운용할 때에는 반드시 필요함)
# bind? 생성된 소켓의 번호와 실제 어드레스 패밀리를 연결해주는 것. 
## bind 함수 내에 '튜플'을 입력함 -> ('',8080)는 (ip,prot)형식으로 한 쌍으로 구성된 어드레스 패밀리의 인자가 된다. 
# 주소에 해당하는 부분에 빈 문자열인 이유? AF_INET에서 ''는 INADDR_ANY를 의미 
#       -> 모든 인터페이스와 연결하고 싶다면 빈 문자열 넣기 (모든 주소로 소켓에 연결 할 수 있음)
# 위 bind는 8080번 포트에서 모든 인터페이스에게 연결하도록 한다 의 의미.

# ==> IPv4의 TCP 통신으로 소켓을 생성한 후 8080번 포트를 오픈함


serverSock.listen(2)
# bind가 끝나고 listen 하는 단계가 필요 -> 상대방의 접속을 기다리는 단계로 넘어가겠단 의미.
# listen도 bind와 마찬가지로 서버 소켓에서만 쓰임
# listen() 의 인자 -> 해당 소켓이 총 몇 개의 동시 접속까지를 허용할 것인지? 
#                     1을 입력하여 단 한 개의 접속만을 허용했음.
#                     인자를 입력하지 않으면 파이썬이 자의적으로 판단해서 임의의 숫자로 listen함
# -> 서버 소켓은 상대방의 접속이 올 때까지 계속 대기하는 상태가 됨. 
print(f'{port}번 포트로 접속 대기중 ... ')


connectionSock, addr = serverSock.accept() # 연결한 클라이언트 소켓 및 정보
# 접속을 수락하고, 그 후에 통신을 하기위해 accept 사용
# accept() - 소켓에 누군가가 접속하여 연결되었을 때에 결과 값이 return 되는 함수
#           -> 소스코드 내에 serverSock.accept()가 있더라도, 누군가가 접속할 때까지 프로그램은 이 부분에서 계속 멈춰있음
#           -> 상대방이 접속함으로써 accept()가 실행되며 return 값으로 새로운 소켓과 상대방의 AF를 전달해주게 됨 

print(f'{addr} 에서 접속이 확인되었습니다.')

"""
data = connectionSock.recv(1024)
print('sever에서 받은 데이터 : ', data.decode('utf-8'))

connectionSock.send('I am a server.'.encode('utf-8'))
print('server >> 메시지를 보냈습니다.')
"""

while True:
    sendData = input('server >>>')
    if sendData == "":
        break
    connectionSock.send(sendData.encode('utf-8'))

    recvData = connectionSock.recv(1024) ## 최대 받을 수 있는 byte 수는 1500
    print('상대방(client): ', recvData.decode('utf-8'))

serverSock.close()
connectionSock.close()
print('ServerSock Colse')

