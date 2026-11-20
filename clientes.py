
# ==============================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: clientes.py
# DESCRIPCION: Gestion y validacion de clientes
# ==============================================

from entidades import Entidad
from excepciones import ClienteInvalidoError
import re


class Cliente(Entidad):
    """
    Clase que representa a un cliente de Software FJ.
    Hereda de la clase abstracta Entidad.
    """

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)

        # Validar nombre
        if not isinstance(nombre, str) or not nombre.strip():
            raise ClienteInvalidoError("El nombre es obligatorio.")

        # Validar correo electronico
        if not isinstance(correo, str) or not re.fullmatch(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            correo
        ):
            raise ClienteInvalidoError("El correo electronico no es valido.")

        # Validar telefono
        if not isinstance(telefono, str) or not re.fullmatch(
            r"\+?[0-9]{7,15}", telefono
        ):
            raise ClienteInvalidoError("El telefono debe contener entre 7 y 15 digitos.")

        # Encapsulacion de datos personales
        self.__nombre = nombre.strip()
        self.__correo = correo.strip()
        self.__telefono = telefono.strip()

    # Propiedades para consultar los datos
    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    # Metodo sobrescrito de la clase Entidad
    def obtener_informacion(self):
        return (
            f"ID: {self.identificador} | "
            f"Nombre: {self.__nombre} | "
            f"Correo: {self.__correo} | "
            f"Telefono: {self.__telefono}"
        )

    # Modificar correo con validacion
    def actualizar_correo(self, nuevo_correo):
        if not isinstance(nuevo_correo, str) or not re.fullmatch(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            nuevo_correo
        ):
            raise ClienteInvalidoError("El nuevo correo no es valido.")

        self.__correo = nuevo_correo.strip()

    def __str__(self):
        return self.obtener_informacion()
