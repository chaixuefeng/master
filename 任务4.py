'''

dict = {"k1":"v1","k2":"v2","k3":"v3"}
#1、请循环遍历出所有的key

for i in dict:
    print(i)

#2、请循环遍历出所有的value
for i in dict:
    print(dict[i])


#3、请在字典中增加一个键值对,"k4":"v4"
dict['k4']= 'v3'
'''

'''
小明去超市购买水果，账单如下
苹果  32.8
香蕉  22
葡萄  15.5

请将上面的数据存储到字典里，可以根据水果名称查询购买这个水果的费用
用水果名称做key，金额做value，创建一个字典

info = {
    '苹果':32.8,
    '香蕉': 22,
    '葡萄': 15.5
}
while 1:
    fruit = input('请输入水果名称：')
    price = input('请输入该水果的价格：')
    info[fruit] = price
    print(info)
    
小明，小刚去超市里购买水果
小明购买了苹果，草莓，香蕉，小刚购买了葡萄，橘子，樱桃，请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。
以姓名做key，value仍然是字典
Friuts = {
    # 水果和单价
    '苹果': 12.3,
    '草莓': 4.5,
    '香蕉': 6.3,
    '葡萄': 5.8,
    '橘子': 6.4,
    '樱桃': 15.8
}
info = {
    '小明': {
        'fruits': {'苹果': 4, '草莓': 13, '香蕉': 10},
        'money': 0
    },
    '小刚': {
        'fruits': {'葡萄': 19, '橘子': 12, '樱桃': 30},
        'money': 0
    }
}
# print(len(info['小明']['fruits']))
name = input('请输入小明或小刚：')
for i in info[name]['fruits']:
    fruits_name = i
    if fruits_name in Friuts:
        info[name]['money'] = info[name]['money'] + info[name]['fruits'][i] * Friuts[fruits_name]
            # print(info['小明']['fruits'])
            # print(Friuts[fruits_name])
print(name, info[name]['money'])

'''

'''

    编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}   （阿里一轮笔试题）
def listNum(a):
    sep = list(set(a))
    dict1 = dict.fromkeys(sep, 0)
    x = 0
    while x < len(sep):
        dict1[sep[x]] = a.count(sep[x])
        x = x + 1
    return dict1


a = [21, 21, 21, 56, 56, 56, 56, 56, 56, 10, 10, 10, 10, 3, 5]
print(listNum(a))
'''

'''
有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["刘备","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700 , "10"]

name = names[0]
name_liu = name[0]
sep = dict.fromkeys([names[i][0] for i in range(len(names))], name[1:])
print(sep)

'''
