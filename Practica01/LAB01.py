"""
#1
import time
import random

class Cronometro:
    def __init__(self):
        self.__inicia = time.time()
        self.__finaliza = time.time()
    def get_inicia(self):
        return self.__inicia
    def get_finaliza(self):
        return self.__finaliza
    def inicia(self):
        self.__inicia = time.time()
    def detener(self):
        self.__finaliza = time.time()
    def lapsoDeTiempo(self):
        return (self.__finaliza - self.__inicia) * 1000

def ordenacion_por_seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

if __name__ == "__main__":
    CANTIDAD = 10000      
    print(f"Generando {CANTIDAD} números aleatorios...")
    numeros = [random.randint(1, 1000000) for _ in range(CANTIDAD)]
    cronometro = Cronometro()
    print("Iniciando ordenación por selección...")
    cronometro.inicia()
    ordenacion_por_seleccion(numeros)
    cronometro.detener()
    print(f"Tiempo transcurrido: {cronometro.lapsoDeTiempo():.2f} milisegundos")
"""
"""
#2
class EcuaciónLineal:
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
    def tieneSolucion(self):
        return (self.__a*self.__d)-(self.__b*self.__c)!=0
    def getX(self):
        return ((self.__e*self.__d)-(self.__b*self.__f))/((self.__a*self.__d)-(self.__b*self.__c))
    def getY(self):
        return ((self.__a*self.__f)-(self.__e*self.__c))/((self.__a*self.__d)-(self.__b*self.__c))
    def visualizar(self):
        if ecli.tieneSolucion():
            print("x =", ecli.getX())
            print("y =", ecli.getY())
        else:
            print("La ecuacion no tiene solución")
a,b,c,d,e,f =map(int,input("Ingrese a,b,c,d,e,f:").split())
ecli=EcuaciónLineal(a,b,c,d,e,f)
ecli.visualizar()
"""
"""
#3
import math
class EcuacionLineal:
    def __init__(self,a,b,c):
        self.__a=a
        self.__b=b
        self.__c=c
    def getDiscriminante(self):
        return self.__b**2 -4*self.__a*self.__c
    def getRaiz1(self):
        return (-self.__b+math.sqrt(self.__b**2 -4*self.__a*self.__c))/(2*self.__a)
    def getRaiz2(self):
        return (-self.__b-math.sqrt(self.__b**2 -4*self.__a*self.__c))/(2*self.__a)
    def visualizar(self):
        if ecuad.getDiscriminante()>0:
            print("La ecuación tiene dos raíces",ecuad.getRaiz1(),"y",ecuad.getRaiz2())
        elif ecuad.getDiscriminante()==0:
            print("La ecuación tiene una raiz",ecuad.getRaiz1())
        else:
            print("La ecuación no tiene raices reales")
a,b,c=map(int,input("Ingrese a,b,c:").split())
ecuad=EcuacionLineal(a,b,c)
ecuad.visualizar()
"""
"""
#4 POO
import math
class Estadistica:
    def __init__(self,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
        self.__x1=x1
        self.__x2=x2
        self.__x3=x3
        self.__x4=x4
        self.__x5=x5
        self.__x6=x6
        self.__x7=x7
        self.__x8=x8
        self.__x9=x9
        self.__x10=x10
    def promedio(self):
        return (self.__x1+self.__x2+self.__x3+self.__x4+self.__x5+self.__x6
                +self.__x7+self.__x8+self.__x9+self.__x10)/10
    def desviacion(self):
        return math.sqrt(((self.__x1-self.promedio())**2 +(self.__x2-self.promedio())**2
                          +(self.__x3-self.promedio())**2 +(self.__x4-self.promedio())**2
                          +(self.__x5-self.promedio())**2 +(self.__x6-self.promedio())**2
                          +(self.__x7-self.promedio())**2 +(self.__x8-self.promedio())**2
                          +(self.__x9-self.promedio())**2 +(self.__x10-self.promedio())**2)/9)
    def visualizar(self):
        print("El promedio es",estad.promedio())
        print("La desviación estandard es",estad.desviacion())
x1,x2,x3,x4,x5,x6,x7,x8,x9,x10=map(float,input().split())
estad=Estadistica(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10)
estad.visualizar()
"""
"""
#4 Programacion Modular-Estructura
import math
def promedio(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
    p=(x1+x2+x3+x4+x5+x6+x7+x8+x9+x10)/10
    return p
def desviacion(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
    p=promedio(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10)
    d=math.sqrt(((x1-p)**2 +(x2-p)**2 +(x3-p)**2 +(x4-p)**2
                +(x5-p)**2 +(x6-p)**2 +(x7-p)**2 +(x8-p)**2
                 +(x9-p)**2 +(x10-p)**2)/9)
    return d
x1,x2,x3,x4,x5,x6,x7,x8,x9,x10=map(float,input().split())
print("El promedio es:",promedio(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10))
print("La desviación estandard es:",desviacion(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10))
"""
