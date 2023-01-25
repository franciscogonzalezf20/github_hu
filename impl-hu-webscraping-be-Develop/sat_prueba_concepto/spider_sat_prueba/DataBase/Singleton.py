
class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if Singleton.__instance == None:
            Singleton.__instance = object.__new__(cls)

        return Singleton.__instance

    def coneccion(self):
        pass

    def desconection(self):
        pass

