import socket
import sys

HOST = 'localhost'
PORT = 10000

def echo_client():
    '''Echo Server 的Client端'''

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((HOST, PORT))
    except socket.error as e:
        print(e)
        sys.exit()

    while True:
        #  接受用户输入数据并发送服务端
        data = input('input > ')

        # 设定推出条件
        if data == 'exit':
            break

        # 发送数据到服务端
        s.sendall(data.encode())

        # 接受服务端数据
        data = s.recv(1024)
        if not data:
            break
        else:
            print(data.decode('utf-8'))

    s.close()


if __name__=='__main__':
    echo_client()

