from abc import abstractmethod
from abc import ABC
"""
class Validador(ABC):

    @abstractmethod
    def validar(self):
        pass

"""

class Validador13Digitos(Validador):
    def validar(self, number: str):
        if len(number) == 13:
            return True
        return False

class Validador8Digitos(Validador):
    def validar(self, number: str):
        if len(number) == 8:
            return True
        return False

class ValidadorFactory:
    def create_validator(self, digitos: int):
        if digitos == 13:
            return Validador13Digitos()
        elif digitos == 8:
            return Validador8Digitos()

class Main:
    def __init__(self):
        self.validador_factory = ValidadorFactory()

    def validar_numero(self, number: str, digitos: int):
        validador = self.validador_factory.create_validator(digitos)
        if validador.validar(number):
            print("El número es válido.")
        else:
            print("El número no es válido.")

main = Main()
main.validar_numero("1234567890123", 13) # El número es válido.
main.validar_numero("12345678", 8) # El número es válido.
main.validar_numero("123456789", 13) # El número no es válido.
