import xlrd

f = xlrd.open_workbook(filename=r"C:\Users\31211\Desktop\测试项目\python\day08【excel表读写】\2020年每个月的销售情况.xlsx",
                       encoding_override=True)


# 获取全年相应的列中的所有值
def lis(n):
    clothing_all = []
    for i in range(0, 12):
        sheet = f.sheet_by_index(i)
        # 获取所有列
        cols = sheet.ncols
        # 获取服装的名字
        clothing = sheet.col_values(n)

        clothing_all = clothing_all + clothing
    # 获取标题
    title = clothing_all[0]
    # 从列表中去除标题
    for i in range(0, 12):
        clothing_all.remove(title)

    return clothing_all


# 获取单月相应的列中的所有值
def li(z, x, n):
    clothing_all = []
    for i in range(z, x):
        sheet = f.sheet_by_index(i)
        # 获取所有列
        cols = sheet.ncols
        # 获取所有相对列表的值
        clothing = sheet.col_values(n)

        clothing_all = clothing_all + clothing
    # 获取标题
    title = clothing_all[0]
    clothing_all.remove(title)

    return clothing_all


# ----------------全年的销售总额--------------------
# 获取价格
money = lis(2)
# 获取销售的数量
quantity = lis(4)
sum_ = 0
# 计算全年销售额
for i in range(len(money)):
    sum_ = sum_ + money[i] * quantity[i]
    sum_ = round(sum_, 1)
print('全年的销售总额为：%s 元' % sum_)

# ----------------每种衣服的销售（件数）占比--------------
print('----------------每种衣服的销售（件数）占比--------------')
# 获取所有的衣服名
all_name = lis(1)
# 衣服名去重
name = list(set(all_name))
# 总的销售量
all_amount = sum(quantity)
amount = 0
for j in range(len(name)):
    for i in range(len(quantity)):

        if name[j] == all_name[i]:
            amount = amount + quantity[i]
    print(name[j], '的占比为： {:.2%}'.format(amount / all_amount))
    amount = 0

# -----------------------每种衣服的月销售（件数）占比-------------------------
for x in range(12):
    dict_ = {}
    print('---------------%s月份的销售占比------------------' % (x + 1))
    lia = li(x, x + 1, 4)
    sum_lia = sum(lia)
    for j in range(len(name)):
        for i in range(len(lia)):

            if name[j] == all_name[i]:
                amount = amount + lia[i]
        print(name[j], '的占比为： {:.2%}'.format(amount / sum_lia))

        amount = 0
# -----------------------------每种衣服的销售额占比--------------------------
print('-----------------------------每种衣服的销售额占比--------------------------')
money_ = 0
for x in name:
    # for j in range(12):
    for i in range(len(quantity)):
        if x == all_name[i]:
            money_ = money_ + quantity[i] * money[i]

    print(x, '的销售额占比为： {:.2%}'.format(money_ / sum_))
    money_ = 0
# ------------------------最畅销的衣服是那种---------------------------
print('------------------------最畅销的衣服是那种---------------------------')
sum__ = 0
sum_1 = 0

for i in name:
    for j in range(len(quantity)):
        if i == all_name[j]:
            sum__ = sum__ + quantity[j]
    if sum_1 <= sum__:
        sum_1 = sum__
        name_ = i
    sum__ = 0
print('最畅销的衣服是：', name_)

# ----------------------------每个季度最畅销的衣服----------------------------
print('----------------------------每个季度最畅销的衣服----------------------------')
_sell = li(2, 5, 4)
_name = li(2, 5, 1)
sum__ = 0
sum_1 = 0

for i in name:
    for j in range(len(_sell)):
        if i == _name[j]:
            sum__ = sum__ + _sell[j]
    if sum_1 <= sum__:
        sum_1 = sum__
        name_ = i
    sum__ = 0
print('春季最畅销的衣服是：', name_)
_sell = li(5, 8, 4)
_name = li(5, 8, 1)
sum__ = 0
sum_1 = 0

for i in name:
    for j in range(len(_sell)):
        if i == _name[j]:
            sum__ = sum__ + _sell[j]
    if sum_1 <= sum__:
        sum_1 = sum__
        name_ = i
    sum__ = 0
print('夏季最畅销的衣服是：', name_)
_sell = li(8, 11, 4)
_name = li(8, 11, 1)
sum__ = 0
sum_1 = 0

for i in name:
    for j in range(len(_sell)):
        if i == _name[j]:
            sum__ = sum__ + _sell[j]
    if sum_1 <= sum__:
        sum_1 = sum__
        name_ = i
    sum__ = 0
print('秋季最畅销的衣服是：', name_)
_sell = li(11, 12, 4) + li(0, 2, 4)
_name = li(11, 12, 1) + li(0, 2, 1)
sum__ = 0
sum_1 = 0

for i in name:
    for j in range(len(_sell)):
        if i == _name[j]:
            sum__ = sum__ + _sell[j]
    if sum_1 <= sum__:
        sum_1 = sum__
        name_ = i
    sum__ = 0
print('冬季最畅销的衣服是：', name_)

# ------------------全年销量最低的衣服----------------------
print('------------------全年销量最低的衣服----------------------')
_sell = li(6, 9, 4)
_name = li(6, 9, 1)
sum__ = 0
sum_1 = 10000000
for i in name:
    for j in range(len(_sell)):
        if i == _name[j]:
            sum__ = sum__ + _sell[j]
    if sum_1 >= sum__:
        sum_1 = sum__
        name_ = i
print('全年销量最低的衣服：', name_)
