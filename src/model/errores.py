
class Excepcion(Exception):
    pass

class ErrorSalarioNoEntero(Exception):
    """Se usa cuando el valor del salario es erroneo."""
    def __init__(self):
        super().__init__(f'El valor del salario es incorrecto.')

class ErrorSalarioMenorDeCero(Exception):
    """Se usa cuando el valor del salario es menor o igual a 0."""
    def __init__(self):
        super().__init__(f'El salario debe ser mayor a 0.')


class ErrorFechaFormatoIncorrecto(Exception):
    """Se usa cuando el formato de la fecha está mal intoducida"""
    """Se usa también cuando se ingresa una fecha de retiro anterior a la de ingreso."""
    def __init__(self):
        super().__init__(f'El formato de la fecha está mal introducido.')
        
class ErrorFechaIncorrecta(Exception):
    """Se usa también cuando se ingresa una fecha de retiro anterior a la de ingreso."""
    def __init__(self):
        super().__init__(f'La fecha de retiro no puede ser anterior a la de ingreso.')