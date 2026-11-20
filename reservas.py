
# ==============================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: reservas.py
# DESCRIPCION: Gestion de reservas
# ==============================================

from entidades import Entidad
from excepciones import (
    ReservaInvalidaError,
    OperacionNoPermitidaError
)


class Reserva(Entidad):
    """Clase que representa una reserva de un servicio."""

    def __init__(self, identificador, cliente, servicio, duracion):
        super().__init__(identificador)

        if cliente is None:
            raise ReservaInvalidaError("Debe seleccionar un cliente.")

        if servicio is None:
            raise ReservaInvalidaError("Debe seleccionar un servicio.")

        try:
            servicio.validar_parametros(duracion)
        except Exception as error:
            raise ReservaInvalidaError(
                "No fue posible validar los datos de la reserva."
            ) from error

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "PENDIENTE"
        self.__costo = 0

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    @property
    def costo(self):
        return self.__costo

    def confirmar(self):
        if self.__estado != "PENDIENTE":
            raise OperacionNoPermitidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.__costo = self.__servicio.calcular_costo(self.__duracion)
        self.__estado = "CONFIRMADA"

        return "Reserva confirmada correctamente."

    def cancelar(self):
        if self.__estado != "PENDIENTE":
            raise OperacionNoPermitidaError(
                "Solo se pueden cancelar reservas pendientes."
            )

        self.__estado = "CANCELADA"
        return "Reserva cancelada correctamente."

    def procesar(self):
        if self.__estado != "CONFIRMADA":
            raise OperacionNoPermitidaError(
                "La reserva debe estar confirmada para procesarse."
            )

        self.__estado = "PROCESADA"
        return "Reserva procesada correctamente."

    def obtener_informacion(self):
        return (
            f"Reserva: {self.identificador} | "
            f"Cliente: {self.__cliente.nombre} | "
            f"Servicio: {self.__servicio.nombre} | "
            f"Duracion: {self.__duracion} | "
            f"Estado: {self.__estado} | "
            f"Costo: ${self.__costo:,.0f}"
        )

    def __str__(self):
        return self.obtener_informacion()
