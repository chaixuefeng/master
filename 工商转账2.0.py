from data import updata, select

Library = {}


def transfer():
    # 转出的账号，转入的账号，转出账号的密码，转出的金额
    out_ID = input('请输入转出的账号：')
    enter_ID = input('请输入转入的账号：')
    out_pw = int(input('请输入转出的账号的密码：'))
    out_money = int(input('请输入转账金额：'))
    reply = bank_treasury(out_ID, enter_ID, out_pw, out_money)
    if reply == 0:
        print('转账成功！')
        print('转账金额为：', out_money)
    elif reply == 1:
        print('您输入的账户不对！')
    elif reply == 2:
        print('密码输入错误！')
    elif reply == 3:
        print('账户金额不足！')


# 首页界面
def front_page():
    print('**********欢迎来到中国建设银行*********')
    print('1、开户')
    print('2、存钱')
    print('3、取钱')
    print('4、转账')
    print('5、查询')
    print('6、Bye')
    print('************************************')


def bank_treasury(out_ID, enter_ID, out_pw, out_money):
    all_data = []
    for i in select():
        data = list(i)
        all_data.append(data)
    # print(all_data)
    for i in all_data:
        Library[i[0]] = i
    # print(Library.keys())
    # 判断账号是否存在：
    if out_ID in Library.keys() and enter_ID in Library.keys():
        if out_pw != Library[out_ID][2]:
            return 2
        elif Library[out_ID][-2] - out_money < 0:
            return 3
        else:

            sql = 'update zhengxuefengshigou set money = money + %s where ID=%s '
            param = [out_money, enter_ID, ]
            updata(sql, param)
            sql = 'update zhengxuefengshigou set  money = money - %s where ID=%s'
            param = [out_money, out_ID]
            updata(sql, param)
            return 0
    else:
        return 1


while True:
    front_page()

    # 输入业务
    business = input('请输入您要办理的业务：')

    if business == '4':
        transfer()
