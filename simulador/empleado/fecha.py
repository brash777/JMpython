class Fecha():
    dia = ''
    mes = ''
    anio = ''
    
    
    
_method_ = 'DarDia'
_parameter_ = 'ninguno'
_return_ = 'dia'
_description_ = 'metodo que regresa el dia'
def DarDia(self):
    return self.dia
    
    

_method_ = 'DarMes'
_parameter_ = 'ninguno'
_return_ = 'mes'
_description_ = 'metodo que regresa el mes'
def DarMes(self):
    return self.mes


_method_ = 'DarAnio'
_parameter_ = 'ninguno'
_return_ = 'anio'
_description_ = 'metodo que regresa el Anio'

def DarAnio(self):
    return self.anio



_method_ = 'DarAnio'
_parameter_ = 'ninguno'
_return_ = 'anio'
_description_ = 'metodo que regresa el Anio'

def DarFecha(self):
    return self.dia + ' / ' + self.mes + ' / ' + self.anio