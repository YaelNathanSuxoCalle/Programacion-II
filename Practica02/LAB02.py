
#1
import math
from multimethod import multimethod
class MiPunto:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y

    @multimethod
    def distancia(self, punto: "MiPunto"):
        dx = self.getX() - punto.getX()
        dy = self.getY() - punto.getY()
        return math.sqrt(dx**2 + dy**2)
    @multimethod
    def distancia(self, x: float, y: float):
        dx = self.getX() - x
        dy = self.getY() - y
        return math.sqrt(dx**2 + dy**2)

p1 = MiPunto()
p2 = MiPunto(10.0, 30.5)
print(f"Punto 1: ({p1.getX()}, {p1.getY()})")
print(f"Punto 2: ({p2.getX()}, {p2.getY()})")
d1 = p1.distancia(p2)
print("Distancia entre p1 y p2:", d1)
d2 = p1.distancia(10.0, 30.5)
print("Distancia usando coordenadas:", d2)

"""
#2
from multimethod import multimethod
class AlgebraVectorial:
  @multimethod
  def __init__(self):
    self.a = [0, 0, 0]
    self.b = [0, 0, 0]
  @multimethod
  def __init__(self, a: list, b: list):
    self.a = a
    self.b = b
    
  def norma(self, v: list):
    return sum(x**2 for x in v) ** 0.5
  def punto(self, u: list, v: list):
    return sum(x * y for x, y in zip(u, v))
  @multimethod
  def perpendicular(self, a: list, b: list, op: str):
    if op == 'a':
      sum_ab = [x + y for x, y in zip(a, b)]
      res_ab = [x - y for x, y in zip(a, b)]
      return round(self.norma(sum_ab), 5) == round(self.norma(res_ab), 5)
    elif op == 'b':
      res_ab = [x - y for x, y in zip(a, b)]
      res_ba = [x - y for x, y in zip(b, a)]
      return round(self.norma(res_ab), 5) == round(self.norma(res_ba), 5)
    elif op == 'c':
      return round(self.punto(a, b), 5) == 0
    elif op == 'd':
      sum_ab = [x + y for x, y in zip(a, b)]
      return round(self.norma(sum_ab) ** 2, 5) == round(
          self.norma(a) ** 2 + self.norma(b) ** 2, 5)
  @multimethod
  def paralela(self, a: list, b: list, r: float):
    return a == [r * x for x in b]
  @multimethod
  def paralela(self, a: list, b: list, op: str):
    cruz = [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    ]
    return cruz == [0, 0, 0]
  def proyeccion(self, a: list, b: list):
    factor = self.punto(a, b) / (self.norma(b) ** 2)
    return [factor * x for x in b]
  def componente(self, a: list, b: list):
    return self.punto(a, b) / self.norma(b)

calc = AlgebraVectorial()
u = [1, 0, 0]
v = [0, 1, 0]
if calc.perpendicular(u, v, 'c'):
	print("Los dos vectores son perpendiculares")
else:
	print("Los dos vectores no son perpendiulares")
if calc.paralela(u, v, 'f'):
	print("Los dos vectores son paralelos")
else:
	print("Los dos vectores no son paralelos")

print("Proyeccion:",calc.proyeccion(u,v))  
print("Componente:",calc.componente(u,v))
"""
"""
#3
class Vector3D:
  def __init__(self, a1: float = 0, a2: float = 0, a3: float = 0):
    self.a1 = float(a1)
    self.a2 = float(a2)
    self.a3 = float(a3)
  def __add__(self, b):
    return Vector3D(self.a1 + b.a1, self.a2 + b.a2, self.a3 + b.a3)
  def __mul__(self, r: float):
    return Vector3D(r * self.a1, r * self.a2, r * self.a3)
  def __rmul__(self, r: float):
    return self.__mul__(r)
  def longitud(self) -> float:
    return (self.a1**2 + self.a2**2 + self.a3**2) ** 0.5
  def normal(self):
    m = self.longitud()
    return Vector3D(self.a1 / m, self.a2 / m, self.a3 / m)
  def producto_escalar(self, b) -> float:
    return self.a1 * b.a1 + self.a2 * b.a2 + self.a3 * b.a3
  def producto_vectorial(self, b):
    return Vector3D(
        self.a2 * b.a3 - self.a3 * b.a2,
        self.a3 * b.a1 - self.a1 * b.a3,
        self.a1 * b.a2 - self.a2 * b.a1,
    )
  def __repr__(self):
    return f'({round(self.a1, 2)}, {round(self.a2, 2)}, {round(self.a3, 2)})'

if __name__ == '__main__':
  a = Vector3D(1, 2, 3)
  b = Vector3D(4, 5, 6)

  print('a + b =', a + b)
  print('3 * a =', 3 * a)  
  print('|a| =', round(a.longitud(), 2))
  print('Normal de a =', a.normal())
  print('a · b =', a.producto_escalar(b))
  print('a x b =', a.producto_vectorial(b))
"""
