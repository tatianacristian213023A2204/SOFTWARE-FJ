
# ==============================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: main.py
# DESCRIPCION: Programa principal del sistema
# ==============================================

import logging
import os

from sistema import SistemaSoftwareFJ
from clientes import Cliente
from servicios import (
    ServicioSala,
    ServicioEquipo,
    ServicioAsesoria
)
from reservas import Reserva

from excepciones import (
    ClienteInvalidoError,
    ServicioInvalidoError,
    ReservaInvalidaError,
    OperacionNoPermitidaError,
    ParametroFaltanteError
)


# Crear carpeta de registros
os.makedirs("logs", exist_ok=True)

# Configurar archivo de registros
logging.basicConfig(
    filename="logs/registro.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True
)


def registrar_evento(mensaje):
    print(mensaje)
    logging.info(mensaje)


def ejecutar_pruebas():

    sistema = SistemaSoftwareFJ()

    print("\n====================================")
    print("       SISTEMA SOFTWARE FJ")
    print("====================================\n")

    # PRUEBA 1: Crear cliente valido
    try:
        cliente1 = Cliente(
            "C001", "Tatiana", "tatiana@gmail.com", "3001234567"
        )
        sistema.registrar_cliente(cliente1)
        registrar_evento("Prueba 1: Cliente creado correctamente.")

    except ClienteInvalidoError as error:
        print("Prueba 1: Error controlado:", error)
        logging.error("Prueba 1: %s", error)

    # PRUEBA 2: Crear segundo cliente valido
    try:
        cliente2 = Cliente(
            "C002", "Cristian", "cristian@gmail.com", "3101234567"
        )
        sistema.registrar_cliente(cliente2)
        registrar_evento("Prueba 2: Segundo cliente creado correctamente.")

    except ClienteInvalidoError as error:
        print("Prueba 2: Error controlado:", error)
        logging.error("Prueba 2: %s", error)

    # PRUEBA 3: Crear cliente con correo incorrecto
    try:
        cliente_malo = Cliente(
            "C003", "Carlos", "correo_incorrecto", "3001234567"
        )

    except ClienteInvalidoError as error:
        print("Prueba 3: Error controlado:", error)
        logging.error("Prueba 3: %s", error)

    finally:
        logging.info("Prueba 3 finalizada.")

    # PRUEBA 3.1: Comprobar parametro obligatorio faltante
    try:
        cliente_sin_id = Cliente(
            None, "Pedro", "pedro@gmail.com", "3001234567"
        )

    except ParametroFaltanteError as error:
        print("Prueba 3.1: Error controlado:", error)
        logging.error("Prueba 3.1: %s", error)

    # PRUEBA 4: Crear servicio de sala
    try:
        sala = ServicioSala(
            "S001", "Sala de reuniones", 50000
        )
        sistema.registrar_servicio(sala)
        registrar_evento("Prueba 4: Servicio de sala creado.")

    except ServicioInvalidoError as error:
        print("Prueba 4: Error controlado:", error)
        logging.error("Prueba 4: %s", error)

    # PRUEBA 5: Crear servicio de equipos
    try:
        equipo = ServicioEquipo(
            "S002", "Alquiler de computador", 30000
        )
        sistema.registrar_servicio(equipo)
        registrar_evento("Prueba 5: Servicio de equipos creado.")

    except ServicioInvalidoError as error:
        print("Prueba 5: Error controlado:", error)
        logging.error("Prueba 5: %s", error)

    # PRUEBA 6: Crear servicio de asesoria
    try:
        asesoria = ServicioAsesoria(
            "S003", "Asesoria profesional", 80000
        )
        sistema.registrar_servicio(asesoria)
        registrar_evento("Prueba 6: Servicio de asesoria creado.")

    except ServicioInvalidoError as error:
        print("Prueba 6: Error controlado:", error)
        logging.error("Prueba 6: %s", error)

    # PRUEBA 6.1: Intentar crear servicio con costo negativo
    try:
        servicio_malo = ServicioSala(
            "S004", "Sala incorrecta", -50000
        )

    except ServicioInvalidoError as error:
        print("Prueba 6.1: Error controlado:", error)
        logging.error("Prueba 6.1: %s", error)

    # PRUEBA 7: Calcular costo sin impuesto ni descuento
    try:
        costo_basico = sala.calcular_costo(2)

        print("Prueba 7: Costo basico:", costo_basico)
        logging.info("Prueba 7: Calculo basico realizado.")

    except ServicioInvalidoError as error:
        print("Prueba 7: Error controlado:", error)
        logging.error("Prueba 7: %s", error)

    # PRUEBA 7.1: Calcular costo con impuesto
    try:
        costo_impuesto = sala.calcular_costo(
            2, impuesto=19
        )

        print("Prueba 7.1: Costo con impuesto:", costo_impuesto)
        logging.info("Prueba 7.1: Calculo con impuesto realizado.")

    except ServicioInvalidoError as error:
        print("Prueba 7.1: Error controlado:", error)
        logging.error("Prueba 7.1: %s", error)

    # PRUEBA 7.2: Calcular costo con impuesto y descuento
    try:
        costo = sala.calcular_costo(
            2, impuesto=19, descuento=10
        )

        print("Prueba 7.2: Costo con impuesto y descuento:", costo)
        logging.info("Prueba 7.2: Calculo con impuesto y descuento realizado.")

    except ServicioInvalidoError as error:
        print("Prueba 7.2: Error controlado:", error)
        logging.error("Prueba 7.2: %s", error)

    # PRUEBA 8: Calcular servicio con duracion incorrecta
    try:
        equipo.calcular_costo(-2)

    except ServicioInvalidoError as error:
        print("Prueba 8: Error controlado:", error)
        logging.error("Prueba 8: %s", error)

    # PRUEBA 8.1: Intentar reservar un servicio no disponible
    try:
        equipo.cambiar_disponibilidad(False)

        reserva_no_disponible = Reserva(
            "R003", cliente1, equipo, 2
        )

        print("Prueba 8.1: La reserva no deberia haberse creado.")

    except ReservaInvalidaError as error:
        print("Prueba 8.1: Error controlado:", error)
        logging.error("Prueba 8.1: %s", error)

    finally:
        equipo.cambiar_disponibilidad(True)
        logging.info("Prueba 8.1 finalizada.")

    # PRUEBA 9: Crear reserva valida
    try:
        reserva1 = Reserva(
            "R001", cliente1, sala, 2
        )
        sistema.registrar_reserva(reserva1)
        registrar_evento("Prueba 9: Reserva creada correctamente.")

    except ReservaInvalidaError as error:
        print("Prueba 9: Error controlado:", error)
        logging.error("Prueba 9: %s", error)

    # PRUEBA 10: Confirmar reserva
    try:
        mensaje = reserva1.confirmar()
        print("Prueba 10:", mensaje)
        logging.info("Prueba 10: Reserva confirmada.")

    except (OperacionNoPermitidaError, ReservaInvalidaError) as error:
        print("Prueba 10: Error controlado:", error)
        logging.error("Prueba 10: %s", error)

    else:
        print("El costo de la reserva es:", reserva1.costo)
        logging.info("Prueba 10: Confirmacion ejecutada sin errores.")

    # PRUEBA 11: Procesar reserva
    try:
        mensaje = reserva1.procesar()
        print("Prueba 11:", mensaje)
        logging.info("Prueba 11: Reserva procesada.")

    except OperacionNoPermitidaError as error:
        print("Prueba 11: Error controlado:", error)
        logging.error("Prueba 11: %s", error)

    # PRUEBA 12: Intentar cancelar reserva procesada
    try:
        reserva1.cancelar()

    except OperacionNoPermitidaError as error:
        print("Prueba 12: Error controlado:", error)
        logging.error("Prueba 12: %s", error)

    # PRUEBA 13: Crear reserva para segundo cliente
    try:
        reserva2 = Reserva(
            "R002", cliente2, equipo, 3
        )
        sistema.registrar_reserva(reserva2)
        registrar_evento("Prueba 13: Segunda reserva creada.")

    except ReservaInvalidaError as error:
        print("Prueba 13: Error controlado:", error)
        logging.error("Prueba 13: %s", error)

    # PRUEBA 14: Cancelar reserva pendiente
    try:
        print("Prueba 14:", reserva2.cancelar())
        logging.info("Prueba 14: Reserva cancelada.")

    except OperacionNoPermitidaError as error:
        print("Prueba 14: Error controlado:", error)
        logging.error("Prueba 14: %s", error)

    # PRUEBA 15: Mostrar informacion del sistema
    print("\n====================================")
    print("       INFORMACION DEL SISTEMA")
    print("====================================")

    print(cliente1.obtener_informacion())
    print(sala.obtener_informacion())
    print(equipo.obtener_informacion())
    print(asesoria.obtener_informacion())
    print(reserva1.obtener_informacion())
    print(reserva2.obtener_informacion())

    sistema.mostrar_resumen()

    print("\nLas pruebas finalizaron.")
    print("Los registros se guardaron en logs/registro.log")


if __name__ == "__main__":
    ejecutar_pruebas()
