
# ==============================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: entidades.py
# DESCRIPCION: Clase abstracta general del sistema
# ==============================================

from abc import ABC, abstractmethod
from excepciones import ParametroFaltanteError


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad general
    del sistema Software FJ.
    """

    def __init__(self, identificador):

        if identificador is None or identificador == "":
            raise ParametroFaltanteError(
                "El identificador es obligatorio."
            )

        if not isinstance(identificador, str):
            raise ParametroFaltanteError(
                "El identificador debe ser texto."
            )

        if not identificador.strip():
            raise ParametroFaltanteError(
                "El identificador no puede contener solo espacios."
            )

        self.__identificador = identificador.strip()

    @property
    def identificador(self):
        return self.__identificador

    @abstractmethod
    def obtener_informacion(self):
        pass

    def __str__(self):
        return f"Entidad: {self.__identificador}"
