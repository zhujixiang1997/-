''''''
'''
1.写一个游乐场门票的类，计算两个成人一个小孩平日票价
​     平日票价100元
​     周末为平日的120%
​     小孩半价S

  4 class Ticket:
  5     def __init__(self,week = False,child = False):
  6         self.exp = 100
  7         if week:
  8             self.inc = 1.2
  9         else:
 10             self.inc = 1
 11         if child:
 12             self.discount = 0.5
 13         else:
 14             self.discount = 1
 15     def calcPrice(self,num):
 16         return (self.exp * self.inc * self.discount * num)
 17
 18 adult = Ticket()
 19 child = Ticket(child=True)
 20 print("2个成人 + 1个小孩平日的票价为：%.2f" % (adult.calcPrice(2) + child.calcPrice(1)))
'''