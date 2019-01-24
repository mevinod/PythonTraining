import threading
import time


def print1_10():
    for i in range(1, 10):
        time.sleep(1)
        print(i)


threading.Thread(target=print1_10).start()