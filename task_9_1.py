import time
from shutil import get_terminal_size

class TrafficLight:
    __color = ['красный', 'жёлтый', 'зелённый']
    def running(self, num=1):
        self.num = num
        time_wait = [7, 2, 5]
        while num != 0:
            for i in range(0, len(time_wait), 2):
                print(self.__color[i])
                time.sleep(time_wait[i])
                print("\n" * get_terminal_size().lines, end='')
                print(self.__color[1])
                time.sleep(time_wait[1])
                print("\n" * get_terminal_size().lines, end='')
            num -= 1

class_1 = TrafficLight()
class_1.running(3)

