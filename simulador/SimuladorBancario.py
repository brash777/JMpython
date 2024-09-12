__author__ = "johan mosquera"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "johan.mosqueram@campusucc.edu.co"
from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from Tiempo import Tiempo

class Banco:
    nombre_cliente = ''
    numero_de_cedula = ''
    cuenta_corriente = CuentaAhorros()
    cuenta_corriente = CuentaCorriente()
    mes_simulacion = Tiempo()
    

def DarNombreCliente(self):
    return self.nombre_cliente

