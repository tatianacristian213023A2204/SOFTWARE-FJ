
# ==============================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: excepciones.py
# DESCRIPCION: Excepciones personalizadas del sistema
# ==============================================

# Excepcion general para el sistema Software FJ
class SoftwareFJError(Exception):
    """Excepcion base del sistema."""
    pass


# Error cuando los datos de un cliente son incorrectos
class ClienteInvalidoError(SoftwareFJError):
    """Se produce cuando los datos del cliente no son validos."""
    pass


# Error cuando un servicio presenta datos incorrectos
class ServicioInvalidoError(SoftwareFJError):
    """Se produce cuando un servicio tiene datos incorrectos."""
    pass


# Error cuando se intenta reservar un servicio no disponible
class ServicioNoDisponibleError(SoftwareFJError):
    """Se produce cuando el servicio no esta disponible."""
    pass


# Error cuando una reserva presenta problemas
class ReservaInvalidaError(SoftwareFJError):
    """Se produce cuando una reserva no cumple las condiciones."""
    pass


# Error cuando se intenta realizar una operacion no permitida
class OperacionNoPermitidaError(SoftwareFJError):
    """Se produce cuando una operacion no esta permitida."""
    pass


# Error cuando faltan parametros obligatorios
class ParametroFaltanteError(SoftwareFJError):
    """Se produce cuando falta un parametro obligatorio."""
    pass
