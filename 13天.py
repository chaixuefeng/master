from threading import Thread

from time import sleep
import time

# 柜子
cabinet = 500
time_ = int(time.time())
all_money = 0

# 厨师
class chef(Thread):
    name = ''
    num = 0

    #     厨师做蛋糕
    def run(self) -> None:
        global cabinet, time_, all_money
        while True:
            time_end = time.time()
            if cabinet < 500 and time_end - time_ < 60:
                cabinet += 1
                self.num += 1

            elif time_end - time_ < 60:
                sleep(3)
            else:
                print('%s 一共做了 %s 个蛋糕，赚了%s元' % (self.name, self.num, self.num * 1.5))
                break


# 客人
class guest(Thread):
    name = ''
    money = 5000
    num = 0

    def run(self) -> None:
        global cabinet, time_, all_money
        while True:
            time_end = time.time()
            if cabinet > 0 and time_end - time_ < 60 and self.money > 3:
                self.money -= 3
                self.num += 1
                cabinet -= 1
                all_money += 3
            elif time_end - time_ < 60 and self.money > 3:
                sleep(2)
            else:
                print('%s一共买了了%s个蛋糕,还剩余%s元' % (self.name, self.num, self.money))
                break


c1 = chef()
c2 = chef()
c3 = chef()
g1 = guest()
g2 = guest()
g3 = guest()
g4 = guest()
g5 = guest()
g6 = guest()

c1.name = '厨师1'
c1.name = '厨师2'
c1.name = '厨师3'
g1.name = '客人1'
g2.name = '客人2'
g3.name = '客人3'
g4.name = '客人4'
g5.name = '客人5'
g6.name = '客人6'
c1.start()
c2.start()
c3.start()

g1.start()
g2.start()
g3.start()
g4.start()
g5.start()
g6.start()
