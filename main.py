class Soda():
    def __init__(self, type):
        if isinstance(type, str):
            self.type = type
        else:
            self.type = None

    def Type_soda(self):
        if self.type:
            print(f'газировка {Soda1.type}')
        else:
            print('обычная газировка')
Soda1 = Soda('кокакола')
Soda2 = Soda(00)

Soda2.Type_soda()
