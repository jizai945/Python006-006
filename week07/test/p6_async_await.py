# python 3.4 支持事件循环的方法
import asyncio

@asyncio.coroutine
def py34_func():
    yield from sth()


########################################
# python3.5 增加async await
async def py35_func():
    await sth()

# 注意：await 接收的对象必须是awaitable对象
# awaitable对象定义了 __await__()方法
# awaitable对象有三类
# 1. 协程coroutine
# 2. 任务Task
# 3. 未来对象Future
########################################
import asyncio
async def main():
    print('hello')
    await asyncio.sleep(3)
    print('world')

# asyncio.run()运行最高层级的conroutine
asyncio.run(main())
# hello
# sleep 3 second
# world

######################################
# 协程调用过程： 
# 调用协程时，会被注册到ioloop，返回coroutine对象
# 用ensure_future 封装为Future对象
# 提交给ioloop

# 官方文档
# https://docs.python.org/zh-cn/3/library/asyncio-task.html
