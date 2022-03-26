from abc import ABC, abstractmethod


class MyAbstractClass(ABC):

    @abstractmethod
    def coat(self, size):
        pass

    @abstractmethod
    def suit(self, height):
        pass


class Clothes(MyAbstractClass):
    size = False
    height = False

    def coat(self, size):
        self.size = size
        return f'Нужно ткани {round(self.size / 6.5, 2) + 0.5}'

    def suit(self, height):
        self.height = height
        return f'Нужно ткани {2 * self.height + 0.3}'

    @property
    def fabric_all(self):
        if self.size == False and self.height == False:
            return 'Еще одежда не выбрана'
        elif not self.height:
            return f'Нужно ткани всего {round(self.size / 6.5, 2) + 0.5}'
        elif not self.size:
            return f'Нужно ткани {2 * self.height + 0.3}'
        else:
            return f'Нужно ткани всего {(round(self.size / 6.5, 2) + 0.5) + (2 * self.height + 0.3)}'


clothe_1 = Clothes()
print(clothe_1.coat(10))
print(clothe_1.suit(8))
print(clothe_1.fabric_all)
