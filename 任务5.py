'''

随机生成1000个整数;
数字范围[20,100];
输出所有不同的数字及其每个数字重复的次数,

有能力的话升序排序打印所有数字{“数字”:”次数”}

import random

list_ = []
i = 0
while i < 1000:
    num = random.randint(20, 100)
    list_.append(num)
    i += 1
list_num = list(set(list_))
dict_num = dict.fromkeys(list_num, 0)
for j in dict_num:
    dict_num[j] = list_.count(j)
print(dict_num)
'''


'''

输出商品列表，用户输入序号，显示用户选中的商品

goods = [{"name": "电脑", "price": 1999},

         {"name": "鼠标", "price": 10},

         {"name": "显示器", "price": 120},

         {"name": "内存", "price": 230}, ]
for i in range(len(goods)):
    print(i, goods[i]['name'], goods[i]['price'])
while True:
    num = input("请输入商品的序号（输入'Q'或者’q‘退出系统）")
    if num == 'q' or num == 'Q':
        break
    nu = int(num)
    if nu in range(len(goods)):
        print(nu , goods[nu]['name'], goods[nu]['price'])
    else:
        print('非法输入')

要求:

1：页面显示 序号 + 商品名称 + 商品价格，如

 1 电脑 1999

 2 鼠标 10

2：用户输入选择的商品序号，然后打印商品名称及商品价格

3：如果用户输入的商品序号有误，则提示输入有误，并重新输入

4：用户输入Q或者q，退出程序
'''
















