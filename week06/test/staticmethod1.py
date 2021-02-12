import datetime


class Story(object):
    snake = 'Python'

    def __init__(self, name):
        self.name = name

    # 静态方法
    @staticmethod
    def god_come_go():
        if not datetime.datetime.now().month % 2:
            print('god is coming')


Story.god_come_go()
