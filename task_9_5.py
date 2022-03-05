class Stationery:
    title = "Канцелярская принадлежность"
    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    """
    из описания не понятно должен ли параметр быть в самом классе или передоваться
    если передоваться то можно модифицировать
    def draw(self, title):
        self.title = title
        print(f"Запуск отрисовки {self.title}")
    """
    title = "ручка"
    def draw(self):
        print(f"Запуск отрисовки {Pen.title}")


class Pencil(Stationery):
    title = "карандаш"
    def draw(self):
        print(f"Запуск отрисовки {Pencil.title}")


class Handle(Stationery):
    title = "маркер"
    def draw(self):
        print(f"Запуск отрисовки {Handle.title}")

class NoteBook(Stationery):
    def draw(self, title):
        self.title = title
        print(f"Запуск отрисовки {self.title}")


class_1 = Stationery()
class_1.draw()

class_2 = Pen()
class_2.draw()

class_3 = Pencil()
class_3.draw()

class_4 = Handle()
class_4.draw()

class_5 = NoteBook()
class_5.draw('Notebook')