import time
import logging
import os

# 编写一个函数, 当函数被调用时，将调用的时间记录在日志中, 日志文件的保存位置建议为：/var/log/python- 当前日期 /xxxx.log

def write_log():
    date = time.strftime('%Y-%m-%d', time.localtime())
    now_dir = os.path.dirname(os.path.abspath(__file__))
    log_file = str(now_dir) + '/var/log/python-' + str(date) + '/test.log'
    log_dir = os.path.dirname(log_file)
    print(log_file)

    if not os.path.exists(log_dir):  # 检测路径是否存在
         os.makedirs(log_dir)
    
    # 默认追加方式
    logging.basicConfig(filename=log_file,
                        level=logging.DEBUG,
                        datefmt='%H:%m:%d %x',
                        format='%(asctime)s %(name)-8s %(levelname)-8s [line: %(lineno)d] %(message)s'
                        )

    logging.debug('debug msg')

if __name__ == "__main__":
    write_log()
    