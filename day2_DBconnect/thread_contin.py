import threading
from threading import *
from time import sleep


class Accent(Thread):
    def run(self):
        for i in range(5):
            print("Accent")
            sleep(2)


class LKM(Thread):
    def run(self):
        for i in range(5):
            print("LKM")
            sleep(2)


obj1 = Accent()
obj2 = LKM()
obj1.start()
obj2.start()


#obj1.join()
#obj2.join()
