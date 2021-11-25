'''

    人类：
        属性:
            姓名，性别，年龄，所拥有的手机剩余话费，手机品牌，手机电池容量，手机屏幕大小，手机最大待机时长，所拥有的积分。
    功能：
        发短信（要求参数传入短信内容）。
        打电话（要求传入要打的电话号码和要打的时间长度。程序里判断号码是否为空或者本人的话费是否小于1元，若为空或者小于1元则报相对应的错误信息，否则的话拨通。结束后，
        按照时间长度扣费并返回扣费（0~10分钟：1元/钟、15个积分/钟，10~20分钟：0.8元/钟、39个积分/钟，其他：0.65元/钟、48个积分/钟））

from time import sleep


class Humanity:
    # 名字
    name = ''
    # 性别
    gender = ''
    # 年龄
    age = ''
    # 话费
    Phone_bill = 10.00
    # 手机品牌
    brand = ''
    # 手机电池容量
    Battery = ''
    # 屏幕大小
    Screen = ''
    # 待机时长
    duration = ''
    # 积分
    integral = 0

    # 发送短信
    def Texting(self):
        # 输入短信内容
        content = input('请输入短信内容：')
        # 请输入要拨打的时长
        time = int(input())

    # 打电弧
    def Call_up(self):

        # 输入电话号码
        num = input('请输入您要拨打的电话号码：')
        # 拨打的时6长
        time = input('请输入您要拨打的时间（分钟)：')
        # 判断电话号码
        if num.isdigit() and self.Phone_bill > 1 and len(num) == 11:
            time = float(time)
            if time > 20:
                self.Phone_bill = self.Phone_bill - time * 0.65
                print('您的话费剩余：', self.Phone_bill)
                self.integral = self.integral + 48 * time
            elif time > 10:
                self.Phone_bill = self.Phone_bill - time * 0.8
                print('您的话费剩余：', self.Phone_bill)
                self.integral = self.integral + 39 * time
            else:
                self.Phone_bill = self.Phone_bill - time * 1
                print('您的话费剩余：', self.Phone_bill)
                self.integral = self.integral + 15 * time
            f = '您正在通话中...'
            for i in f:
                print(i)
                time = int(time)
                sleep(time * 60 / 9)

        elif self.Phone_bill <= 1:
            print('您已欠费请即使充值！')
        else:
            print('您拨打的空号！')


H = Humanity()
H.Call_up()
'''

'''
i.定义了一个学生类：属性:学号，姓名，年龄，性别，身高，体重，成绩，家庭地址，电话号码。行为：学习（要求参数传入学习的时间），
玩游戏（要求参数传入游戏名），编程（要求参数传入写代码的行数），数的求和（要求参数用变长参数来做，返回求和结果）
class student:
    # 学号
    student_ID = ''
    # 学生名字
    name = ''
    # 年龄
    # age = ''
    # 性别
    gender = '男'
    # 身高
    height = ''
    # 体重
    weight = ''
    # 成绩
    score = ''
    # 家庭住址
    family_address = ''
    # 电话号码
    phone_number = ''

    def learn(self):
        time = input('传入学习的时间：')
        print('%s学习的时间是：%s' % (self.name, time))

    def play_games(self):
        game_name = input('请输入游戏名称：')
        print('%s玩的游戏名叫：%s' % (self.name, game_name))

    def programming(self):
        num = input('请输入代码的行数：')
        print('%s一共写了%s行代码' % (self.name, num))

    def sum(self, *nums):
        print('nums: ', nums)

        sum = 0
        for num in nums:
            sum += num

        print('sum = ', sum)
        return sum
    

ii.车类：属性：车型号，车轮数，车身颜色，车重量，油箱存储大小 。功能：跑（要求参数传入车的具体功能，比如越野，赛车）
创建：法拉利，宝马，铃木，五菱，拖拉机对象
class car:
    # 车型号
    Car_model = ''
    # 车轮胎数
    num = ''
    # 车身颜色
    colour = ''
    # 车身重量
    weight = ''
    # 油箱大小
    tank = ''

    def run(self, name):
        # name = input('请输入什么车：')
        print('%s在马路上跑' % (name))


c = car()

iii.笔记本电脑：属性：型号，待机时间，颜色，重量，cpu型号，内存大小，硬盘大小。  行为：打游戏（传入游戏的名称）,办公。
class computer:
    # 型号
    model = ''
    # 待机时长
    time = ''
    # 颜色
    color = ''
    # 重量
    weight = ''
    # cpu
    cpu = ''
    # 内存大小
    RAM = ''
    # 硬盘
    hard_disk = ''

    def play_game(self, name):
        print('型号:%s待机时长:%s颜色:%s重量:%sCPU:%s内存大小:%s硬盘:%s的电脑运行%s' % (
        self.model, self.time, self.color, self.weight, self.cpu, self.RAM, self.hard_disk, name))
    
    def Office(self):
        print('型号:%s待机时长:%s颜色:%s重量:%sCPU:%s内存大小:%s硬盘:%s的电脑办公' % (
            self.model, self.time, self.color, self.weight, self.cpu, self.RAM, self.hard_disk))
iv.猴子类：属性：类别，性别，身体颜色，体重。行为：造火（要求传入造火的材料：比如木棍还是石头），学习事物（要求参数传入学习的具体事物，可以不止学习一种事物）
class monkey:
    # 类型
    category = ''
    # 性别
    gender = ''
    # 身体颜色
    Body_color = ''
    # 体重
    weight = ''

    def fire(self, material):
        print('%s的猴,%s性,颜色为%s,体重为%s，正在用%s来生火' % (self.category, self.gender, self.Body_color, self.weight, material))

    def Learn(self, *thing):
        for i in thing:
            print('%s的猴,%s性,颜色为%s,体重为%s，正在用%s来生火' % (self.category, self.gender, self.Body_color, self.weight, i))

'''





