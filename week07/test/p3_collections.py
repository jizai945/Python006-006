# 命名元组
from collections import deque
from collections import Counter
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, y=20)
p.x+p.y
p[0] + p[1]
x, y = p


# 计数器
mystring = ['a', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'e']
# 取得频率最高的前三个值
cnt = Counter(mystring)
cnt.most_common(3)
cnt['b']

# 双向队列
d = deque('uvw')
d.append('xyz')
d.appendleft('rst')
