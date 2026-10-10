"""
#1
import random
class Juego:
    def __init__(self, numeroDeVidas):
        self.__numeroDeVidas = numeroDeVidas
        self.__vidasIniciales = numeroDeVidas
        self.__record = 0
    def reiniciaPartida(self):
        self.__numeroDeVidas = self.__vidasIniciales
    def actualizaRecord(self):
        if self.__numeroDeVidas > self._record:
            self.__record = self.__numeroDeVidas
    def quitaVida(self):
        self.__numeroDeVidas = self.__numeroDeVidas - 1
        if self.__numeroDeVidas > 0:
            return True
        else:
            return False
    def getNumeroDeVidas(self):
        return self.__numeroDeVidas
    def getRecord(self):
        return self.__record

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.__numeroAdivinar = 0
    def juega(self):
        self.reiniciaPartida()
        self.__numeroAdivinar = random.randint(0, 10)
        while True:
            numero = int(input("Adivina un número entre 0 y 10: "))
            if numero == self.__numeroAdivinar:
                print("¡Acertaste!")
                self.actualizaRecord()
                print("Récord de vidas restantes:", self.getRecord())
                return
            else:
                quedanVidas = self.quitaVida()
                if quedanVidas:
                    if numero < self.__numeroAdivinar:
                        print("El número a adivinar es mayor.")
                    else:
                        print("El número a adivinar es menor.")
                    print("Vidas restantes:", self.getNumeroDeVidas())
                else:
                    print("Te has quedado sin vidas.")
                    print("El número era:", self.__numeroAdivinar)
                    return

class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()
Aplicacion.main()
"""
"""
#2
import random
class Juego:
    def __init__(self, numeroDeVidas):
        self.__numeroDeVidas = numeroDeVidas
        self.__vidasIniciales = numeroDeVidas
        self.__record = 0
    def reiniciaPartida(self):
        self.__numeroDeVidas = self.__vidasIniciales
    def actualizaRecord(self):
        if self.__numeroDeVidas > self.__record:
            self.__record = self.__numeroDeVidas
    def quitaVida(self):
        self.__numeroDeVidas = self.__numeroDeVidas - 1
        if self.__numeroDeVidas > 0:
            return True
        else:
            return False
    def getNumeroDeVidas(self):
        return self.__numeroDeVidas
    def getRecord(self):
        return self.__record

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.__numeroAdivinar = 0
    def generaNumero(self):
        return random.randint(0, 10
    def validaNumero(self, numero):
        if numero >= 0 and numero <= 10:
            return True
        else:
            print("Error: el número debe estar entre 0 y 10.")
            return False
    def juega(self):
        self.reiniciaPartida()
        self.__numeroAdivinar = self.generaNumero()
        while True:
            try:
                numero = int(input("Adivina un número entre 0 y 10: "))
            except ValueError:
                print("Error: debes introducir un número entero.")
            else:
                if self.validaNumero(numero):
                    if numero == self.__numeroAdivinar:
                        print("¡Acertaste!")
                        self.actualizaRecord()
                        print("Récord:", self.getRecord())
                        return
                    else:
                        quedanVidas = self.quitaVida()
                        if quedanVidas:
                            if numero < self.__numeroAdivinar:
                                print("El número a adivinar es mayor.")
                            else:
                                print("El número a adivinar es menor.")
                            print("Vidas restantes:",
                                  self.getNumeroDeVidas())
                        else:
                            print("Te has quedado sin vidas.")
                            print("El número era:",
                                  self.__numeroAdivinar)
                            return

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def generaNumero(self):
        return random.choice([0, 2, 4, 6, 8, 10])
    def validaNumero(self, numero):
        if numero < 0 or numero > 10:
            print("Error: el número debe estar entre 0 y 10.")
            return False
        elif numero % 2 != 0:
            print("Error: debes introducir un número par.")
            return False
        else:
            return True

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def generaNumero(self):
        return random.choice([1, 3, 5, 7, 9])
    def validaNumero(self, numero):
        if numero < 0 or numero > 10:
            print("Error: el número debe estar entre 0 y 10.")
            return False
        elif numero % 2 == 0:
            print("Error: debes introducir un número impar.")
            return False
        else:
            return True

class Aplicacion:
    @staticmethod
    def main():
        juego1 = JuegoAdivinaNumero(3)
        juego2 = JuegoAdivinaPar(3)
        juego3 = JuegoAdivinaImpar(3)
        print("\n--- Juego de adivinar cualquier número ---")
        juego1.juega()
        print("\n--- Juego de adivinar números pares ---")
        juego2.juega()
        print("\n--- Juego de adivinar números impares ---")
        juego3.juega()
Aplicacion.main()
"""
#3
class Sensor:
    # Atributo de clase
    tipo = "Genérico"

    def __init__(self, id):
        # Atributos de instancia
        self.id = id
        self.encendido = False

    def activar(self):
        self.encendido = True

    def desactivar(self):
        self.encendido = False


class Camara(Sensor):
    # Atributo de clase
    tipo = "Cámara"

    def __init__(self, id, resolucion):
        super().__init__(id)
        # Atributo de instancia
        self.resolucion = resolucion


class SensorLuzLaser(Sensor):
    # Atributo de clase
    tipo = "Luz Laser"

    def __init__(self, id, alcance):
        super().__init__(id)
        # Atributo de instancia
        self.alcance = alcance


class VehiculoAutonomo(Camara, SensorLuzLaser):
    tipo = "Vehículo Autónomo"

    def __init__(self, id, resolucion, alcance):
        Sensor.__init__(self, id)
        self.resolucion = resolucion
        self.alcance = alcance

def main():
    sensor = Sensor("S01")
    camara = Camara("C01", "4K")
    laser = SensorLuzLaser("L01", 100)
    vehiculo = VehiculoAutonomo("V01", "Full HD", 150)
    print("--- SENSOR ---")
    print("Tipo:", sensor.tipo)
    print("ID:", sensor.id)
    print("Encendido:", sensor.encendido)
    print("\n--- CÁMARA ---")
    print("Tipo:", camara.tipo)
    print("ID:", camara.id)
    print("Resolución:", camara.resolucion)
    print("\n--- SENSOR LUZ LÁSER ---")
    print("Tipo:", laser.tipo)
    print("ID:", laser.id)
    print("Alcance:", laser.alcance)
    print("\n--- VEHÍCULO AUTÓNOMO ---")
    print("Tipo:", vehiculo.tipo)
    print("ID:", vehiculo.id)
    print("Resolución:", vehiculo.resolucion)
    print("Alcance:", vehiculo.alcance)
    print("Encendido:", vehiculo.encendido)
    vehiculo.activar()
    print("Después de activar:", vehiculo.encendido)
    vehiculo.desactivar()
    print("Después de desactivar:", vehiculo.encendido)
main()
