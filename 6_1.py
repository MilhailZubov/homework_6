from time import sleep
from itertools import cycle

class TrafficLight:
    def __init__(self):
        self.__color = (('Красный', 7), ('Желтый', 2), ('Зеленый', 6))
    def run(self):
        for color, sec, in cycle(self.__color):
            print(color, 'waiting {} sec'.format(sec))
            sleep(sec)
traffic_light = TrafficLight()
traffic_light.run()