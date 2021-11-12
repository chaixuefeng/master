Library = {"1": {"name": 1,
                 "password": 123456,
                 "country": 1,
                 "province": 1,
                 "street": 1,
                 "door": 1,
                 "money": 100,
                 "bank_name": 1},
           "2": {"name": 1,
                 "password": 123456,
                 "country": 1,
                 "province": 1,
                 "street": 1,
                 "door": 1,
                 "money": 100,
                 "bank_name": 1}, }
def transfer():
    # 转出的账号，转入的账号，转出账号的密码，转出的金额
    out_ID = input('请输入转出的账号：')
    enter_ID = input('请输入转入的账号：')
    out_pw = int(input('请输入转出的账号的密码：'))
    out_money = int(input('请输入转账金额：'))
    reply = bank_treasury(out_ID, enter_ID, out_pw, out_money)
    if reply == 0:
        print('转账成功！')
        print('您的账户余额为：', Library[out_ID]["money"])
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
    # 判断账号是否存在：
    if out_ID in Library and enter_ID in Library:

        if out_pw != Library[out_ID]["password"]:
            return 2
        elif Library[out_ID]["money"] - out_money < 0:
            return 3
        else:
            Library[out_ID]["money"] = Library[out_ID]["money"] - out_money
            Library[enter_ID]["money"] = Library[enter_ID]["money"] + out_money
            return 0
    else:
        return 1



while True:
    front_page()

    # 输入业务
    business = input('请输入您要办理的业务：')

    if business == '4':
        transfer()
