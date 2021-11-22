import random
from data import updata, select, insert
from pip._vendor.distlib.compat import raw_input

Library = {}


# 添加用户
def add_user():
    ID = str(random.randint(10000000, 99999999))
    name = raw_input('请输入姓名')
    password = input('请输入密码：')
    country = input("亲输入您国籍：")
    province = input("亲输入您的省份：")
    street = input("亲输入您的街道：")
    door = input("亲输入您的门牌号：")
    money = float(input("亲输入您的初始账户余额："))
    bank_name = '中国工商银行'
    while True:
        if password.isdigit() and len(password) == 6:

            param = [ID, name, password, country, province, street, door, money, bank_name]
            insert(param)
            print('''
            --------注册账户提示---------

                *恭喜您账户创建成功！*
            您的账号为：%s

            ---------------------------
            ''' % ID)
            break

        else:
            print('''
            --------注册账户提示---------

                账号请输入六位纯数字密码！


            ---------------------------
            ''')
            password = input('请输入密码：')


# 存钱
def Save_money():
    # 输入账号和密码
    user_ID = input('请输入账号：')
    user_money = int(input('请输入存取金额：'))
    all_data = []
    for i in select():
        data = list(i)
        all_data.append(data)
    # print(all_data)
    for i in all_data:
        Library[i[0]] = i
    # 判断账号是否存与库中
    if user_ID in Library.keys():
        sql = 'update zhengxuefengshigou set money = money + %s where ID=%s '
        param = [user_money, user_ID]
        updata(sql, param)
        print('''
        ------------中国工商银行-----------
        
            *恭喜您存款成功！*
        
           
        ----------------------------------       
        ''')
        # print(Library)  # 查看库
    else:
        print('''
        ------------中国工商银行-----------
        
            存款失败！！！
        
           
        ----------------------------------    
        ''')


# 取款
def Withdraw_money():
    # 输入账号、密码、取款金额
    user_ID = input('请输入账号：')
    user_pw = int(input('请输入密码：'))
    user_money = int(input('请输入取款金额：'))
    all_data = []
    for i in select():
        data = list(i)
        all_data.append(data)
    # print(all_data)
    for i in all_data:
        Library[i[0]] = i
    # 判断ID是否存在与库中
    if user_ID not in Library.keys():
        print('''
        ----------中国工行银行---------
            提示：
                账号不存在！
                
                
        ''')
    # 判断密码是否正确
    elif user_pw != Library[user_ID][2]:
        print('''
        ----------中国工行银行---------
            提示：
                密码输入错误！
                
                
        ''')
    elif Library[user_ID][-2] - user_money < 0:
        print('''
        ----------中国工行银行---------
            提示：
                余额不足！
                
                
        ''')
    else:
        sql = 'update zhengxuefengshigou set money = money - %s where ID=%s '
        param = [user_money, user_ID]
        updata(sql, param)
        # Library[user_ID][-2] = Library[user_ID][-2] - user_money
        print('''
        ----------中国工行银行---------
            提示：
                取款成功！
                
                
        ''')


# 转账
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


#  账户信息查询
def Inquire():
    user_ID = input('请输入账号：')
    user_pw = int(input('请输入密码：'))
    all_data = []
    for i in select():
        data = list(i)
        all_data.append(data)
    # print(all_data)
    for i in all_data:
        Library[i[0]] = i
    if user_ID in Library.keys():
        if user_pw == Library[user_ID][2]:
            print('''
            ------------个人账户信息-------------
            
            当前账号：%s 
            姓名：%s
            密码：%s 
            余额；%0.2f 元 
            国籍：%s 
            省：%s 
            街道：%s 
            门牌：%s 
            开户行：%s 
            
            ''' % (user_ID, Library[user_ID][1], Library[user_ID][2],
                   Library[user_ID][-2], Library[user_ID][3], Library[user_ID][4], Library[user_ID][5],
                   Library[user_ID][6], Library[user_ID][-1]))
        else:
            print('密码输入错误！')
    else:
        print('该用户不存在！')


print('''
-----------------中国工商银行昌平支行----------------

1、开户
2、存款
3、取款
4、转账
5、查询
6、退出
--------------------------------------------------
''')

while True:
    num = input('请输入您要办理的业务编号:')
    if num == '1':
        all_data = []
        for i in select():
            data = list(i)
            all_data.append(data)
            # print(all_data)
        for i in all_data:
            Library[i[0]] = i
        li = list(Library.keys())
        if len(li) < 000:
            add_user()
        else:
            print('用户库已满！')
    elif num == '2':
        Save_money()
    elif num == '3':
        Withdraw_money()
    elif num == '4':
        transfer()
    elif num == '5':
        Inquire()
    elif num == '6':
        print('''
        -----------中国工商银行-----------
            
            *谢谢使用中国建设银行系统！*
            
            
        ''')
        break