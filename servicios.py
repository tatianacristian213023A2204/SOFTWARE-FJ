# ==============================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: servicios.py
# DESCRIPCION: Gestion de los servicios de la empresa
# ==============================================

from abc import ABC, abstractmethod
from entidades import Entidad
from excepciones import ServicioInvalidoError


class Servicio(Entidad, ABC):
    """
    Clase abstracta que representa los servicios
    ofrecidos por Software FJ.
    """

    def __init__(self, identificador, nombre, costo_base):
        super().__init__(identificador)

        if not isinstance(nombre, str) or not nombre.strip():
            raise ServicioInvalidoError("El nombre del servicio es obligatorio.")

        if not isinstance(costo_base, (int, float)) or costo_base <= 0:
            raise ServicioInvalidoError("El costo base debe ser mayor que cero.")

        self.nombre = nombre.strip()
        self.costo_base = costo_base

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
        return f"{self.nombre} - Costo base: ${self.costo_base:,.0f}"


class ServicioSala(Servicio):
    """Servicio de reserva de salas."""

    def validar_parametros(self, duracion):
        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ServicioInvalidoError("La duracion de la sala debe ser mayor que cero.")

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)
        subtotal = self.costo_base * duracion
        total = subtotal + (subtotal * impuesto / 100) - (subtotal * descuento / 100)
        return total

    def describir_servicio(self):
        return "Reserva de sala por horas para reuniones y actividades."


class ServicioEquipo(Servicio):
    """Servicio de alquiler de equipos."""

    def validar_parametros(self, duracion):
        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ServicioInvalidoError("La duracion del alquiler debe ser mayor que cero.")

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)
        subtotal = self.costo_base * duracion
        total = subtotal + (subtotal * impuesto / 100) - (subtotal * descuento / 100)
        return total

    def describir_servicio(self):
        return "Alquiler de equipos tecnologicos por horas o jornadas."


class ServicioAsesoria(Servicio):
    """Servicio de asesorias especializadas."""

    def validar_parametros(self, duracion):
        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ServicioInvalidoError("La duracion de la asesoria debe ser mayor que cero.")

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)
        subtotal = self.costo_base * duracion
        total = subtotal + (subtotal * impuesto / 100) - (subtotal * descuento / 100)
        return total

    def describir_servicio(self):
        return "Asesoria especializada brindada por profesionales."


print("Servicios de Software FJ cargados correctamente.")