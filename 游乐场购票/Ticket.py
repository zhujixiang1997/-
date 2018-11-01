class Ticket:
    def __init__(self):
        self.piaojia = 100

    def choose(self):
        print('==========欢迎来到方特欢乐世界！！！==========')
        print('请选择你要进行的操作：1.购票 2.退出')
        cz = input('请输入你要进行的操作：')
        if cz == '1':
            print('请选择你要购买的票种类：1.成人票  2.儿童票')
            piao = input('请输入你要进行的操作：')
            if piao == '1':
                pass
        elif cz == '2':
            print('欢迎下次来玩！')
            exit()
        else:
            print('请输入正确数字')





T1 = Ticket()
T1.choose()