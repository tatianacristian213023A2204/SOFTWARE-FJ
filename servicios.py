
# ==============================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: servicios.py
# DESCRIPCION: Gestion de los servicios de la empresa
# ==============================================

from abc import ABC, abstractmethod
import math

from entidades import Entidad
from excepciones import (
    ServicioInvalidoError,
    ServicioNoDisponibleError
)


class Servicio(Entidad, ABC):
    """
    Clase abstracta que representa los servicios
    ofrecidos por Software FJ.
    """

    def __init__(self, identificador, nombre, costo_base):
        super().__init__(identificador)

        if not isinstance(nombre, str) or not nombre.strip():
            raise ServicioInvalidoError(
                "El nombre del servicio es obligatorio."
            )

        if (
            not isinstance(costo_base, (int, float))
            or isinstance(costo_base, bool)
            or not math.isfinite(costo_base)
            or costo_base <= 0
        ):
            raise ServicioInvalidoError(
                "El costo base debe ser un numero mayor que cero."
            )

        self.nombre = nombre.strip()
        self.costo_base = costo_base
        self.__disponible = True

    @property
    def disponible(self):
        return self.__disponible

    def cambiar_disponibilidad(self, estado):
        if not isinstance(estado, bool):
            raise ServicioInvalidoError(
                "La disponibilidad debe ser True o False."
            )

        self.__disponible = estado

    def verificar_disponibilidad(self):
        if not self.__disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {self.nombre} no esta disponible."
            )

    def validar_porcentajes(self, impuesto, descuento):

        for nombre, valor in (
            ("impuesto", impuesto),
            ("descuento", descuento)
        ):
            if (
                not isinstance(valor, (int, float))
                or isinstance(valor, bool)
                or not math.isfinite(valor)
                or valor < 0
                or valor > 100
            ):
                raise ServicioInvalidoError(
                    f"El {nombre} debe estar entre 0 y 100."
                )

    def calcular_costo_base(self, duracion, impuesto=0, descuento=0):

        self.verificar_disponibilidad()
        self.validar_parametros(duracion)
        self.validar_porcentajes(impuesto, descuento)

        subtotal = self.costo_base * duracion

        total = (
            subtotal
            + (subtotal * impuesto / 100)
            - (subtotal * descuento / 100)
        )

        if not math.isfinite(total) or total < 0:
            raise ServicioInvalidoError(
                "El resultado del calculo no es valido."
            )

        return total

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        pass

    def obtener_informacion(self):
        estado = (
            "Disponible" if self.__disponible
            else "No disponible"
        )

        return (
            f"{self.nombre} - Costo base: ${self.costo_base:,.0f}"
            f" - Estado: {estado}"
        )


class ServicioSala(Servicio):
    """Servicio de reserva de salas."""

    def validar_parametros(self, duracion):
        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or not math.isfinite(duracion)
            or duracion <= 0
        ):
            raise ServicioInvalidoError(
                "La duracion de la sala debe ser mayor que cero."
            )

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        return self.calcular_costo_base(
            duracion, impuesto, descuento
        )

    def describir_servicio(self):
        return (
            "Reserva de sala por horas para reuniones y actividades."
        )


class ServicioEquipo(Servicio):
    """Servicio de alquiler de equipos."""

    def validar_parametros(self, duracion):
        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or not math.isfinite(duracion)
            or duracion <= 0
        ):
            raise ServicioInvalidoError(
                "La duracion del alquiler debe ser mayor que cero."
            )

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        return self.calcular_costo_base(
            duracion, impuesto, descuento
        )

    def describir_servicio(self):
        return (
            "Alquiler de equipos tecnologicos por horas o jornadas."
        )


class ServicioAsesoria(Servicio):
    """Servicio de asesorias especializadas."""

    def validar_parametros(self, duracion):
        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or not math.isfinite(duracion)
            or duracion <= 0
        ):
            raise ServicioInvalidoError(
                "La duracion de la asesoria debe ser mayor que cero."
            )

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        return self.calcular_costo_base(
            duracion, impuesto, descuento
        )

    def describir_servicio(self):
        return (
            "Asesoria especializada brindada por profesionales."
        )


print("Servicios de Software FJ cargados correctamente.")
