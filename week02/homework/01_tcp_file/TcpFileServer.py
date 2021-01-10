# 实现服务端和客户端可以传输单个文件的功能

import socket
import os
from pathlib import Path
from time import sleep

HOST = 'localhost'
PORT = 6666

def tcp_file_server():
    ''' TCP传输文件服务端''' 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 将对象s绑定到指定的主机和端口上
    s.bind((HOST, PORT))
    # 只接受一个连接
    s.listen(1)

    while True:
        print('wait connect')
        # accept表示接受用户端的连接
        conn, addr = s.accept()
        # 输出客户端地址
        print(f'Connected by {addr}')
        while True:
            try:
                cmd = conn.recv(128)
            except Exception as e:
                print(e)
                break

            cmd = cmd.decode()
            if not cmd:
                break

            # 1.判断命令
            # -> send:文件从客户端传输到服务端
            # -> recv:文件从服务端传输到客户端
            # -> exit:断开客户端连接
            # 2. 执行命令功能 

            # 文件从 客户端传输到服务端
            if cmd == 'send':
                print('send cmd')
                recv_file_name = conn.recv(128).decode()
                print(recv_file_name)
                if recv_file_name == 'exit':
                    pass
                else:
                    now_dir = os.path.dirname(os.path.abspath(__file__))
                    recv_file =  str(now_dir) + '/server/' + str(recv_file_name)
                    file_dir = os.path.dirname(recv_file)
                    print(recv_file)

                    if not os.path.exists(file_dir):  # 检测路径是否存在
                        os.makedirs(file_dir)

                    
                    size = int(conn.recv(128).decode())
                    print(f'file size:{size}')
                    # 二进制方式写文件
                    with open(recv_file, 'wb') as f:
                        while size > 0:
                            data = conn.recv(128)
                            size -= len(data)
                            f.write(data)

                        print('文件接收完成')    



            # 文件从 客户端传输到服务端
            elif cmd == 'recv':
                print('recv cmd')
                send_file_name = conn.recv(128).decode()
                print(send_file_name)
                now_dir = os.path.dirname(os.path.abspath(__file__))
                send_file = str(now_dir) + '/server/' + send_file_name;
                my_file = Path(send_file)
                # 判断文件是否存在
                if not my_file.is_file():
                    conn.sendall('exit'.encode())
                else:
                    size = os.path.getsize(my_file)              
                    conn.sendall(str(size).encode())
                    sleep(1)

                    # 二进制方式读文件
                    with open(my_file, 'rb+') as f:
                        while True:
                            data = f.read(128)
                            conn.sendall(data)
                            if len(data) < 128:
                                break;

                        print('文件发送完成')   

            # 断开客户端连接
            elif cmd == 'exit':
                break

        print('connect close')
        conn.close()    


    s.close()           





    s.close()    

if __name__ == '__main__':
    tcp_file_server()
