# Magic methods (dunder methods)

class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        # class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'{class_name}(x= {self.x!r}, y= {self.y!r}, z= {self.z!r})'
    
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)
    
p1 = Ponto(1, 2)
p2 = Ponto(5, 6)

print(p1)
print(p2)

p3 = p1 + p2
print(p3)