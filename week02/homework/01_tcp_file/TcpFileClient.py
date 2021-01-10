# 实现服务端和客户端可以传输单个文件的功能

import socket
import sys
from time import sleep
import os
from pathlib import Path


HOST = 'localhost'
PORT = 6666

def tcp_file_client():
    '''TCP传输文件 的Client端'''

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((HOST, PORT))
    except socket.error as e:
        print(e)
        sys.exit()

    while True:
        #  接受用户输入数据并发送服务端
        data = input('请输入命令 : \n<send>: 文件传输到服务端\n<recv>: 从服务端获取文件\n<exit>: 断开客户端连接\n> ')

        if not data:
            break

        # 设定推出条件
        if data == 'exit':
            s.sendall(data.encode())
            break
        
        elif data == 'recv':
            s.sendall(data.encode())
            filename = input('请输入要从服务器获取的文件名字> ')
            s.sendall(filename.encode())

            size = s.recv(128).decode()
            if size == 'exit':
                print('服务器找不到该文件')
                pass
            else:
                length = int(size)
                print(f'file size:{length}')

                now_dir = os.path.dirname(os.path.abspath(__file__))
                recv_file =  str(now_dir) + '/client/' + str(filename)
                file_dir = os.path.dirname(recv_file)
                print(recv_file)

                if not os.path.exists(file_dir):  # 检测路径是否存在
                    os.makedirs(file_dir)

                 # 二进制方式写文件
                with open(recv_file, 'wb') as f:
                    while length > 0:
                        data = s.recv(128)
                        length -= len(data)
                        f.write(data)

                    print('文件接收完成')      

        elif data == 'send':
            s.sendall(data.encode())
            data = input('请输入本地文件路径> ')
            print(data)
            # 判断文件是否存在
            my_file = Path(data)
            if not my_file.is_file():
                print('file not found')
                s.sendall('exit'.encode())
            else:
                s.sendall(my_file.name.encode())
                size = os.path.getsize(my_file)              
                s.sendall(str(size).encode())
                sleep(1)
                # 二进制方式读文件
                with open(my_file, 'rb+') as f:
                    while True:
                        data = f.read(128)
                        s.sendall(data)
                        if len(data) < 128:
                            break;

                    print('文件发送完成')   

        else:
            print('请输入正确命令')
        

    s.close()


if __name__=='__main__':
    tcp_file_client()



