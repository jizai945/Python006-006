# grpcio 是启动gRPC 服务的项目依赖
# pip install grpcio
# gRPC tools 包含 protocol buffer 编译器和用于从.proto 文件生成服务端和哭护短代码的插件
# pip install grpcio-tools
# 升级protobuf
# pip install --upgrade protobuf -i https://pypi.douban.com/simple

import grpc
import time
import schema_pb2
import schema_pb2_grpc
from concurrent import futures


# 继承父类 schema_pb2_grpc
class GetwayServer(schema_pb2_grpc.GatewayServicer):

    def Call(self, request_iterator, context):
        for req in request_iterator:
            yield schema_pb2.Response(num=req.num+1)  # num是proto中定义的num
            time.sleep(1)


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    schema_pb2_grpc.add_GatewayServicer_to_server(GetwayServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    main()
