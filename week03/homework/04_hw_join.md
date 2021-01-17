# problem 4

## 问题：

以下两张基于 id 列，分别使用 INNER JOIN、LEFT JOIN、 RIGHT JOIN 的结果是什么?

**Table1**

id name

1 table1_table2

2 table1

**Table2**

id name

1 table1_table2

3 table2

举例: INNER JOIN

```sql
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
INNER JOIN Table2
ON Table1.id = Table2.id;

```





## 回答：

==三者不同：==

```
SQL INNER JOIN 关键字
在表中存在至少一个匹配时，INNER JOIN 关键字返回行。

SQL LEFT JOIN 关键字
LEFT JOIN 关键字会从左表  那里返回所有的行，即使在右表  中没有匹配的行。

SQL RIGHT JOIN 关键字
RIGHT JOIN 关键字会右表 那里返回所有的行，即使在左表  中没有匹配的行。
```



 INNER JOIN

```sql
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
INNER JOIN Table2
ON Table1.id = Table2.id;
```

查询结果：
取交集，即满足`Table1.id = Table2.id`的所有值。



LEFT JOIN

```sql
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
LEFT JOIN Table2
ON Table1.id = Table2.id;
```

查询结果：
返回左表`Table1`所有记录+右表`Table2`满足`on`条件的记录，不满足的，如`Table2.id`，`Table2.name` 列会显示为`NULL`。



RIGHT JOIN

```
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
RIGHT JOIN Table2
ON Table1.id = Table2.id;
```

查询结果：
返回右表`Table1`所有记录+左表`Table2`满足`on`条件的记录，不满足的，如`Table1.id`，`Table1.name` 列会显示为`NULL`。

