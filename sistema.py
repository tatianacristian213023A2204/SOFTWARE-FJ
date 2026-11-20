
# ==============================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: sistema.py
# DESCRIPCION: Administracion general del sistema
# ==============================================

from clientes import Cliente
from servicios import Servicio
from reservas import Reserva
from excepciones import SoftwareFJError


class SistemaSoftwareFJ:
    """
    Clase encargada de administrar clientes,
    servicios y reservas.
    """

    def __init__(self):
        self.__clientes = []
        self.__servicios = []
        self.__reservas = []

    def registrar_cliente(self, cliente):
        try:
            if not isinstance(cliente, Cliente):
                raise SoftwareFJError(
                    "Debe registrar un objeto Cliente valido."
                )

            if any(
                c.identificador == cliente.identificador
                for c in self.__clientes
            ):
                raise SoftwareFJError(
                    "Ya existe un cliente con ese identificador."
                )

            self.__clientes.append(cliente)
            return True

        except SoftwareFJError as error:
            print(f"Error al registrar cliente: {error}")
            return False

    def registrar_servicio(self, servicio):
        try:
            if not isinstance(servicio, Servicio):
                raise SoftwareFJError(
                    "Debe registrar un objeto Servicio valido."
                )

            if any(
                s.identificador == servicio.identificador
                for s in self.__servicios
            ):
                raise SoftwareFJError(
                    "Ya existe un servicio con ese identificador."
                )

            self.__servicios.append(servicio)
            return True

        except SoftwareFJError as error:
            print(f"Error al registrar servicio: {error}")
            return False

    def registrar_reserva(self, reserva):
        try:
            if not isinstance(reserva, Reserva):
                raise SoftwareFJError(
                    "Debe registrar un objeto Reserva valido."
                )

            if any(
                r.identificador == reserva.identificador
                for r in self.__reservas
            ):
                raise SoftwareFJError(
                    "Ya existe una reserva con ese identificador."
                )

            self.__reservas.append(reserva)
            return True

        except SoftwareFJError as error:
            print(f"Error al registrar reserva: {error}")
            return False

    @property
    def clientes(self):
        return self.__clientes.copy()

    @property
    def servicios(self):
        return self.__servicios.copy()

    @property
    def reservas(self):
        return self.__reservas.copy()

    def mostrar_resumen(self):
        print("\n--- RESUMEN DEL SISTEMA ---")
        print(f"Clientes registrados: {len(self.__clientes)}")
        print(f"Servicios registrados: {len(self.__servicios)}")
        print(f"Reservas registradas: {len(self.__reservas)}")
