import random
from time import sleep

money = 1000
num = int(input('猜猜我心里想的数字:'))
randint = random.randint(0, 100)
while 1:
    while money > 0:
        if num == randint:
            print('恭喜你猜对了！')
            print('你是我肚子里的小蛔虫吗？')
            print('可惜没有奖励！')
            money = money - 500
        elif num > randint:
            print('大了大了，往小的猜！')
            money = money - 500
            num = int(input('在试试把！'))
        else:
            print('小了小了，往大的猜！')
            num = int(input('在试试把！'))
            money = money - 500
    print('余额不足')
    print('两秒后自动跳转支付页面！')
    sleep(2)
    print('账号’17688888888‘转账500元获取游戏币！')
    sleep(1)
    money = int(input('请输入充值金额：'))
    while money < 500:
        if  money < 500:
            print('玩一次500，你也太抠了！！！')
            money = int(input('请重新输入充值金额：'))
    num = int(input('可以重新猜了！'))

