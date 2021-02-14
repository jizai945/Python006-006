# 迭代器有效性测试
a_dict = {'a':1, 'b':2}
a_dict_iter = iter(a_dict)

next(a_dict_iter)

a_dict['c'] = 3
next(a_dict_iter)
# RuntimeError: 字典进行插入操作后，字典迭代器会立即失效
a_list = [1, 2, 3, 4, 5]
a_list_iter = iter(a_list)

next(a_list_iter)

a_list.append(6)
next(a_list_iter)
# 尾插入操作不会损坏指向当前元素的List迭代器，列表会自动变长

# 迭代器一旦耗尽，永久损坏
x = iter([ y for y in range(5)])
for i in x:
    i
x.__next__()
