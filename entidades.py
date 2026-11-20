
# ==============================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: entidades.py
# DESCRIPCION: Clase abstracta general del sistema
# ==============================================

from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad general
    del sistema Software FJ.
    """

    def __init__(self, identificador):
        if not identificador:
            raise ValueError("El identificador no puede estar vacio.")

        self.__identificador = identificador

    # Propiedad para consultar el identificador
    @property
    def identificador(self):
        return self.__identificador

    # Metodo abstracto para obtener informacion
    @abstractmethod
    def obtener_informacion(self):
        pass

    # Representacion general de la entidad
    def __str__(self):
        return f"Entidad: {self.__identificador}"
