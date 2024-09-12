__author__ = "johan mosquera"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "johan.mosqueram@campusucc.edu.co"


class CDT:
    saldo_a_invertir = 0
    valor_interes = 0
    
    
_method_ = 'SaldoAInvertir'
_parameter_ = 'nuevoSaldo'
_return_ = 'None'
_description_ = 'Establece un nuevo saldo a invertir en el CDT'
def SaldoAInvertir(self, nuevoSaldo):

    self.Saldo_a_invertir = nuevoSaldo
    return self.Saldo_a_invertir    


_method_ = 'ActualizarSaldoPorMes'
_parameter_ = 'None'
_return_ = 'None'
_description_ = 'Actualiza el saldo del CDT aplicando el interés mensual correspondiente'
def  ActualizarSaldoPorMes():
   return    
    


    