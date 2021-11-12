'''
有下列人员数据库，请按要求实现
# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
]

1.统计每个人的平均薪资

2.统计每个人的平均年龄


3.公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中



4.统计公司男女人数



5.每个部门的人数


names = [
    # 姓名  年龄  性别  编号   任职公司   薪资   部门编号
    ["曹操", "56", "男", "106", "IBM", 500, "50"],
    ["大乔", "19", "女", "230", "微软", 501, "60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700, "10"]
]

sum = 0
age = 0
num = 0
NumberOfPeople = 0
# 计算平均薪资和平均年龄
for i in range(0, 4):
    sum = sum + names[i][5]
    age = age + int(names[i][1])

print('平均薪资:', sum / 4)
print('平均年龄:', age / 4)
# 添加新员工
names.append(["刘备", "45", "男", "220", "alibaba", 500, "30"])
print(names)
# 查看男女人数
for i in range(0, 5):
    if "男" in names[i][2]:
        num += 1
print('男：', num)
print('女：', len(names) - num)
# 查看每个部门的人数
for j in (50, 60, 10):
    for i in range(0, 5):
        if j == int(names[i][-1]):
            NumberOfPeople += 1

    print(j,"人数：",NumberOfPeople)
    NumberOfPeople = 0
'''
'''

现在魔法学院有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。但是呢，因为
有些魔法作业有一定难度，教授不强制同学们必须上交，所以大家上交作业的次数并不一致。

求每个人的总成绩？

sum = 0
names = [['罗恩', 23, 35, 44],
         ['哈利', 60, 77, 68, 88, 90],
         ['赫敏', 97, 99, 89, 91, 95, 90],
         ['马尔福', 100, 85, 90]]
for i in range(0, 4):

    for j in range(1, len(names[i])):
        sum = sum + names[i][j]
    print(sum)
    sum = 0
'''
'''
1、当输入54321时，写出下面程序的执行结果。

num = int(input())
while num!=0:
    print(num%10)
    num = num//10

结果：
1
2
3
4
5

'''
'''

请对下列列表进行冒泡排序（网易测试开发笔试题）

a = [5, 2, 4, 7, 9, 1, 3, 5, 4, 0, 6, 1, 3]
n = len(a)
for i in range(0, n):
    for j in range(0, n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print("排序后的数组:")
for i in range(len(a)):
    print(a[i])

'''