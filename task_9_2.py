class Road:
    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width

    def weight_road(self, weight=25, thickness=1):
        self.weight = weight
        self.thickness = thickness
        weight_all_road = self._lenght * self._width * self.weight * self.thickness
        print(
            f'На дорогу длинной {self._lenght} м. и ширинной {self._width} м. асфальта нужно массой {weight_all_road / 1000} т.')


class_1 = Road(5000, 20)
class_1.weight_road(25, 5)
