# 容器序列的拷贝问题

import copy


old_list = [i for i in range(1, 11)]

new_list1 = old_list
new_list2 = list(old_list)
# 这两个不是同一个列表
print(new_list1 is new_list2)  # False


# 切片操作
new_list3 = old_list[:]
print(new_list3 is old_list)  # False


# 嵌套对象
old_list.append([11, 12])
print(old_list)
print(new_list1)
print(new_list2)
print(new_list3)


new_list4 = copy.copy(old_list)  # 浅拷贝
new_list5 = copy.deepcopy(old_list)  # 深拷贝

assert new_list4 == new_list5  # True
assert new_list4 is new_list5  # False

old_list[10][0] = 13
print(old_list)
print(new_list4)  # 浅拷贝，已跟随变化
print(new_list5)
