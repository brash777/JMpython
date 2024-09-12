___author__ = "johan mosquera"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "johan.mosqueram@campusucc.edu.co"

class CuentaAhorros:
    saldo = 0
    numero_cuenta = ''
    interes_mensual = 0

_method_ = 'ConsignarValor'
_parameter_ = 'nuevoValor'
_return_ = 'valor consignado'
_description_ = 'Depositar un valor a la cuenta.'
def ConsignarValor(self, nuevoValor):
    self.saldo = nuevoValor
    
    
    
_method_ = 'DarSaldo'
_parameter_ = 'ninguno'
_return_ = 'saldo'
_description_ = 'retorna el saldo actual de la cuenta del cliente'
def DarSaldo(self):
    
    return self.saldo


_method_ = 'RetirarValor'
_parameter_ = 'monto'
_return_ = 'valor retirado'
_description_ = 'se retira una cantidad de dinero si la cuenta cuenta con dinero suficiente'
def RetirarValor(self, monto):

    self.saldo = monto



_method_ = 'DarInteresMensual'
_parameter_ = 'ninguno'
_return_ = 'interes mensual'
_description_ = 'retorna el interes mensual ganado'
def DarInteresMensual(self):
    
    return self.interes_mensual


    
_method_ = 'actualizarSaldoPorPasoMes'
_parameter_ = 'ninguno'
_return_ = ''
_description_ = 'actualiza el saldo de la cuenta aumentando el interes mensual'    
def actualizarSaldoPorPasoMes(self):

    return