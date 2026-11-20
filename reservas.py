
# ==============================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: reservas.py
# DESCRIPCION: Gestion de reservas
# ==============================================

from entidades import Entidad
from clientes import Cliente
from servicios import Servicio

from excepciones import (
    ReservaInvalidaError,
    OperacionNoPermitidaError,
    ServicioNoDisponibleError
)


class Reserva(Entidad):

    def __init__(self, identificador, cliente, servicio, duracion):
        super().__init__(identificador)

        if not isinstance(cliente, Cliente):
            raise ReservaInvalidaError(
                "La reserva necesita un cliente valido."
            )

        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError(
                "La reserva necesita un servicio valido."
            )

        try:
            servicio.verificar_disponibilidad()
            servicio.validar_parametros(duracion)

        except ServicioNoDisponibleError as error:
            raise ReservaInvalidaError(
                "No se puede reservar un servicio no disponible."
            ) from error

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

        try:
            self.__servicio.verificar_disponibilidad()

            costo_calculado = self.__servicio.calcular_costo(
                self.__duracion
            )

            if (
                not isinstance(costo_calculado, (int, float))
                or isinstance(costo_calculado, bool)
                or costo_calculado < 0
            ):
                raise ReservaInvalidaError(
                    "El costo calculado no es valido."
                )

            self.__costo = costo_calculado
            self.__estado = "CONFIRMADA"

            return "Reserva confirmada correctamente."

        except ServicioNoDisponibleError as error:
            raise ReservaInvalidaError(
                "No se puede confirmar: el servicio no esta disponible."
            ) from error

    def cancelar(self):

        if self.__estado != "PENDIENTE":
            raise OperacionNoPermitidaError(
                "Solo se pueden cancelar reservas pendientes."
            )

        self.__estado = "CANCELADA"
        self.__costo = 0

        return "Reserva cancelada correctamente."

    def procesar(self):

        if self.__estado != "CONFIRMADA":
            raise OperacionNoPermitidaError(
                "Solo se pueden procesar reservas confirmadas."
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
