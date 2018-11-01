#!/usr/bin/python
# coding:utf8

import random as r

legal_x = [0,10]
legal_y = [0,10]

class Turtle:
     def __init__(self):
          self.power = 100                             #初始化体力
          self.x = r.randint(legal_x[0],legal_x[1])    #初始化位置随机
          self.y = r.randint(legal_y[0],legal_y[1])

     def move(self):
         new_x = self.x + r.choice([1,2,-1,-2])        #随机计算方向 并移动到新的位置(x,y)
         new_y = self.y + r.choice([1,2,-1,-2])

         if new_x < legal_x[0]:                        #检查移动后是否超出了场景x轴边界
             self.x = legal_x[0] - (new_x - legal_x[0])
         elif new_x > legal_x[1]:
             self.x = legal_x[1] - (new_x - legal_x[1])
         else:
             self.x = new_x

         if new_y < legal_y[0]:                        #检查移动后是否超出了场景y轴边界
             self.y = legal_y[0] - (new_y - legal_y[0])
         elif new_y > legal_y[1]:
             self.y = legal_y[1] - (new_y - legal_y[1])
         else:
             self.y = new_y

         self.power -= 1                               #体力消耗
         return (self.x,self.y)                        #返回移动后新的位置

     def eat(self):
         self.power += 20
         if self.power > 100:
             self.power = 100

class Fish:
     def __init__(self):
         self.x = r.randint(legal_x[0],legal_x[1])    #初始化位置随机
         self.y = r.randint(legal_y[0],legal_y[1])

     def move(self):
         new_x = self.x + r.choice([1,-1])            #随机计算方向 并移动到新的位置(x,y)
         new_y = self.y + r.choice([1,-1])

         if new_x < legal_x[0]:                        #检查移动后是否超出了场景x轴边界
             self.x = legal_x[0] - (new_x - legal_x[0])
         elif new_x > legal_x[1]:
             self.x = legal_x[1] - (new_x - legal_x[1])
         else:
             self.x = new_x

         if new_y < legal_y[0]:                        #检查移动后是否超出了场景y轴边界
            self.y = legal_y[0] - (new_y - legal_y[0])
         elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
         else:
            self.y = new_y
            return (self.x,self.y)                        #返回移动后新的位置

turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print("鱼吃完了，游戏结束")
        break
    if not turtle.power:
        print("乌龟体力耗尽")
        break

    pos = turtle.move()
    for each_fish in fish[:]:
         if each_fish.move() == pos:
            turtle.eat()                              #鱼儿被吃掉了
            fish.remove(each_fish)
            print("有一条鱼被吃了")