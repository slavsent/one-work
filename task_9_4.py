class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f'Машина {self.name} поехала')
    def stop(self):
        print(f'Машина {self.name} остановилась')
    def turn(self, direction):
        self.direction = direction
        print(f'Машина {self.name} повернула на {self.direction}')
    def swow_speed(self):
        print(f'Машина {self.name} едит со скоростью {self.speed}')

class TownCar(Car):
    def swow_speed(self):
        if self.speed > 60:
            print(f'Машина {self.name} едит со скоростью {self.speed} - вы превысили допустимую скорость')
        else:
            print(f'Машина {self.name} едит со скоростью {self.speed}')

class SportCar(Car):
    pass

class WorkCar(Car):
    def swow_speed(self):
        if self.speed > 40:
            print(f'Машина {self.name} едит со скоростью {self.speed} - вы превысили допустимую скорость')
        else:
            print(f'Машина {self.name} едит со скоростью {self.speed}')

class PoliceCar(Car):
    def police_car(self):
        if self.is_police:
            print('Это полицейская машина')

auto_1 = Car(40, 'blue', 'BMW 512', False)
print(auto_1.name, auto_1.color, auto_1.speed, auto_1.is_police)
auto_1.go()
auto_1.turn('right')
auto_1.stop()
auto_1.swow_speed()

auto_2 = SportCar(100, 'red', 'Audi Q7', False)
print(auto_2.name, auto_2.color, auto_2.speed, auto_2.is_police)
auto_2.go()
auto_2.turn('left')
auto_2.stop()
auto_2.swow_speed()

auto_3 = TownCar(50, 'green', 'Lada Vesta', False)
print(auto_3.name, auto_3.color, auto_3.speed, auto_3.is_police)
auto_3.go()
auto_3.turn('right')
auto_3.stop()
auto_3.swow_speed()

auto_3_1 = TownCar(80, 'wight', 'Honda Civic', False)
print(auto_3_1.name, auto_3_1.color, auto_3_1.speed, auto_3_1.is_police)
auto_3_1.go()
auto_3_1.turn('right')
auto_3_1.stop()
auto_3_1.swow_speed()

auto_4 = PoliceCar(90, 'grey', 'BMW X5', True)
print(auto_4.name, auto_4.color, auto_4.speed, auto_4.is_police)
auto_4.go()
auto_4.turn('right')
auto_4.stop()
auto_4.swow_speed()
auto_4.police_car()

auto_5 = WorkCar(30, 'black', 'Porshe 911', False)
print(auto_5.name, auto_5.color, auto_5.speed, auto_5.is_police)
auto_5.go()
auto_5.turn('left')
auto_5.stop()
auto_5.swow_speed()

auto_5_1 = WorkCar(70, 'yellow', 'Toyota Colora', False)
print(auto_5_1.name, auto_5_1.color, auto_5_1.speed, auto_5_1.is_police)
auto_5_1.go()
auto_5_1.turn('right')
auto_5_1.stop()
auto_5_1.swow_speed()

