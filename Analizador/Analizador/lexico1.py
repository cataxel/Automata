import ply.lex as lex

class AnalizadorLexico:
    # Lista de tokens
    tokens = (
        'Reser',
        'Float',
        'Num',
        'Id',
        'Char',
        'Sym',
    )

    # Reglas de los tokens
    def t_Reser(self, t):
        r'int|float|char'
        return t

    def t_Float(self, t):
        r'\d+\.\d+'
        t.value = float(t.value)
        return t

    def t_Num(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_Char(self, t):
        r"'.'"
        return t

    def t_Id(self, t):
        r'[a-zA-Z_]\w*'
        return t

    def t_Sym(self, t):
        r'[,;+\-*/()=]'
        return t

    # Caracteres ignorados (espacios y saltos de línea)
    t_ignore = ' \t\n'

    # Manejo de errores
    def t_error(self, t):
        raise CaracterNoReconocidoError(t.value[0], t.lexpos)

    # Construir el analizador léxico
    def analizar(self, input):
        ana = lex.lex(module=self)
        ana.input(input)
        return ana


# Clase para la excepción de caracter no válido
class CaracterNoReconocidoError(Exception):
    def __init__(self, caracter, ubicacion):
        self.caracter = caracter
        self.ubicacion = ubicacion
        if caracter == "'":
            super().__init__(f"No se encontró la ' de cierre en la ubicación: {ubicacion}")
        else:
            super().__init__(f"Carácter no reconocido: {caracter} en la ubicación: {ubicacion}")

        