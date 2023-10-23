import token


terminales_no_terminales = ["id", "num", "int", "float", "char", ",", ";", "+", "-", "*", "/", "(", ")", "=", "$", "P", "Tipo", "V", "A", "S", "E", "T", "F"]
ESTADOS = ["I0", "I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9", "I10", "I11", "I12", "I13", "I14", "I15", "I16", "I17", "I18", "I19", "I20", "I21", "I22", "I23", "I24", "I25", "I26", "I27", "I28", "I29", "I30", "I31", "I32", "I33", "I34", "I35", "I36", "I37"]

tabla = [
        #"id",   "num",    "int",   "float",    "char",   ",",   ";",   "+",   "-",   "*",  "/",   "(",   ")",    "=",   "$",    "P",    "Tipo",     "V",    "A",    "S",    "E",   "T",  "F"]
        [ "I7",     "",     "I4",      "I5",      "I6",    "",    "",    "",    "",    "",    "",    "",    "",    "",    "",    "I1",    "I2",       "",    "I3",    "",     "",    "",    ""],
        ["",        "",     "",        "",       "",       "",    "",    "",    "",    "",    "",    "",    "",    "",    "P0",  "",       "",       "",    "",       "",     "",    "",    ""],
        ["I8",     "",     "",        "",       "",       "",    "",    "",    "",    "",    "",    "",    "",    "",    "",    "",       "",       "",    "",       "",     "",    "",    ""],
        ["",        "",     "",        "",       "",       "",    "",    "",    "",    "",    "",    "",    "",    "",    "P2",  "",       "",       "",    "",       "",     "",    "",    ""],
        ["P3",      "",     "",        "",       "",       "",    "",    "",    "",    "",    "",    "",    "",    "",    "",    "",       "",       "",    "",       "",     "",    "",    ""],
        ["P4",      "",     "",        "",       "",       "",    "",    "",    "",    "",    "",    "",    "",    "",    "",    "",       "",       "",    "",       "",     "",    "",    ""],
        ["P5",      "",     "",        "",       "",       "",    "",    "",    "",    "",    "",    "",    "",    "",    "",    "",       "",       "",    "",       "",     "",    "",    ""],
        ["",        "",     "",        "",       "",       "I9", "",    "",    "",    "",    "",    "",    "",    "",    "",    "",       "",       "",    "",       "",     "",    "",    ""],
        ["",        "",     "",        "",       "",       "",    "I11", "I12", "",    "",    "",    "",    "",    "",    "",    "",       "",       "I10", "",       "",     "",    "",    ""],
        ["I20",     "I21",  "",        "",       "",       "",    "",    "",    "I14", "I15", "",    "",    "I19", "",    "",    "",       "",       "",    "",       "I13",  "I16", "I17", "I18"],
        ["",        "",     "",        "",       "",       "",    "",    "",    "",    "",    "",    "",    "",    "",    "P1",  "",       "",       "",    "",       "",     "",    "",    ""],
        ["I22",     "",     "",        "",       "",       "",    "",    "",    "",    "",    "",    "",    "",    "",    "",    "",       "",       "",    "",       "",     "",    "",    ""],
        ["I7",     "",     "I4",     "I5",    "I6",    "",    "",    "",    "",    "",    "",    "",    "",    "",    "",    "I23",    "I2",    "",    "I3",    "",     "",    "",    ""],
        ["",        "",     "",        "",       "",       "",    "",    "I24", "",    "",    "",    "",    "",    "",    "",    "",       "",       "",    "",       "",     "",    "",    ""],
        ["I20",     "I21",  "",        "",       "",       "",    "",    "",    "",    "",    "",    "",    "I19", "",    "",    "",       "",       "",    "",       "",     "I25", "I17", "I18"],
        ["I20",     "I21",  "",        "",       "",       "",    "",    "",    "",    "",    "",    "",    "I19", "",    "",    "",       "",       "",    "",       "",     "I26", "I17", "I18"],
        ["",        "",     "",        "",       "",       "",    "",    "P11", "I27", "I28", "",    "",    "",    "",    "",    "",       "",       "",    "",       "",     "",    "",    ""],
        ["",        "",     "",        "",       "",       "",    "",    "P14", "P14", "P14", "I29", "I30", "",    "P14", "",    "",       "",       "",    "",       "",     "",    "",    ""],
        ["",        "",     "",        "",       "",       "",    "",    "P17", "P17", "P17", "P17", "P17", "",    "P17", "",    "",       "",       "",    "",       "",     "",    "",    ""],
        ["I20",     "I21",  "",        "",       "",       "",    "",    "",    "",    "",    "",    "",    "I19", "",    "",    "",       "",       "",    "",       "",     "I31", "I17", "I18"],
        ["",        "",     "",        "",       "",       "",    "",    "P19", "P19", "P19", "P19", "P19", "",    "P19", "",    "",       "",       "",    "",       "",     "",    "",    ""],
        ["",        "",     "",        "",       "",       "",    "",    "P20", "P20", "P20", "P20", "P20", "",    "P20", "",    "",       "",       "",    "",       "",     "",    "",    ""],
        ["",        "",     "",        "",       "",       "",    "I11", "I12", "",    "",    "",    "",    "",    "",    "",    "",       "",       "I32", "",       "",     "",    "",    ""],
        ["",        "",     "",        "",       "",       "",    "",    "",    "",    "",    "",    "",    "",    "",    "P7",  "",       "",       "",    "",       "",     "",    "",    ""],
        ["",        "",     "",        "",       "",       "",    "",    "",    "",    "",    "",    "",    "",    "",    "P8",  "",       "",       "",    "",       "",     "",    "",    ""],
        ["",        "",     "",        "",       "",       "",    "",    "P9", "I27", "I28", "",    "",    "",    "",    "",    "",       "",       "",    "",       "",     "",    "",    ""],
        ["",        "",     "",        "",       "",       "",    "",    "P10", "I27", "I28", "",    "",    "",    "",    "",    "",       "",       "",    "",       "",     "",    "",    ""],
        ["I20",     "I21",  "",        "",       "",       "",    "",    "",    "",    "",    "",    "",    "I19", "",    "",    "",       "",       "",    "",       "",     "",    "I33", "I18"],
        ["I20",     "I21",  "",        "",       "",       "",    "",    "",    "",    "",    "",    "",    "I19", "",    "",    "",       "",       "",    "",       "",     "",    "I34", "I18"],
        ["I20",     "I21",  "",        "",       "",       "",    "",    "",    "",    "",    "",    "",    "I19", "",    "",    "",       "",       "",    "",       "",     "",    "",    "I35"],
        ["I20",     "I21",  "",        "",       "",       "",    "",    "",    "",    "",    "",    "",    "I19", "",    "",    "",       "",       "",    "",       "",     "",    "",    "I36"],
        ["",        "",     "",        "",       "",       "",    "",    "",    "I27", "I28", "",    "",    "",    "I37", "",    "",       "",       "",    "",       "",     "",    "",    ""],
        ["",        "",     "",        "",       "",       "",    "",    "",    "",    "",    "",    "",    "",    "",    "P6",  "",       "",       "",    "",       "",     "",    "",    ""],
        ["",        "",     "",        "",       "",       "",    "",    "P12", "P12", "P12", "I29", "I30", "",    "P12", "",    "",       "",       "",    "",       "",     "",    "",    ""],
        ["",        "",     "",        "",       "",       "",    "",    "P13", "P13", "P13", "I29", "I30", "",    "",    "",    "",       "",       "",    "",       "",     "",    "",    ""],
        ["",        "",     "",        "",       "",       "",    "",    "P15", "P15", "P15", "P15", "P15", "",    "P15", "",    "",       "",       "",    "",       "",     "",    "",    ""],
        ["",        "",     "",        "",       "",       "",    "",    "P16", "P16", "P16", "P16", "P16", "",    "P16", "",    "",       "",       "",    "",       "",     "",    "",    ""],
        ["",        "",     "",        "",       "",       "",    "",    "P18", "P18", "P18", "P18", "P18", "",    "P18", "",    "",       "",       "",    "",       "",     "",    "",    ""],
]                  

class AnalizadorSintactico:
    def __init__(self):
        self.producciones = {
            "P0": ("P'", "P", 2),
            "P1": ("P", "Tipo Id V", 6),
            "P2": ("P", "A",2),
            "P3": ("Tipo", "int",2),
            "P4": ("Tipo", "float",2),
            "P5": ("Tipo", "char",2),
            "P6": ("V", ", id V",6),
            "P7": ("V", "; P",4),
            "P8": ("A", "id = S ;",8),
            "P9": ("S", "+ E",6),
            "P10": ("S", "- E",6),
            "P11": ("S", " E",4),
            "P12": ("E", "E + T",6),
            "P13": ("E", "E - T",6),
            "P14": ("E", "T",0),
            "P15": ("T", "T * F",4),
            "P16": ("T", "T / F",6),
            "P17": ("T", "F",6),
            "P18": ("F", "( E )",0),
            "P19": ("F", "id",2),
            "P20": ("F", "num",2),
        }

        self.pila = ["$", "I0"]
        self.estado_actual = ""

    def analisis(self, tokens):
        for token in tokens:
            if token == self.pila[-1]:
                pila_str = ",".join(map(str, self.pila))
                print("Entrada " + token + " pila: (" + pila_str + " ) la cadena se acepta")
                break

            accion = self.obtener_fila_columna(self.estado_actual, token)
            if self.errores(accion):
                break

            print("estado actual: " + self.estado_actual + " accion: " + accion)

            if accion in self.producciones:
                self.aplicar_produccion(accion)
            else:
                self.desplazar(token, accion)

        return self.estado_actual

    def obtener_fila_columna(self, estado_actual, token):
        fila = next((i for i, estado in enumerate(ESTADOS) if estado_actual == estado), None)
        columna = next((i for i, item in enumerate(terminales_no_terminales) if token == item), None)

        return tabla[fila][columna]

    def errores(self, accion):
        if accion == "error ":
            if self.estado_actual == "q32":
                print("Error")
            return True
        return False

    def aplicar_produccion(self, accion):
        pila_str = ",".join(map(str, self.pila))
        acciones = self.producciones[accion]
        acciones_str = ' '.join(map(str, acciones))
        print("Entrada " + token + " pila: (" + pila_str + " ) " + accion + ":" + acciones_str)

        for _ in range(0, acciones[2]):
            self.pila.pop()

        if acciones[0] == "P'":
            self.pila.pop()
        else:
            accion = self.obtener_fila_columna(self.pila[-1], acciones[0])
            self.pila.extend([acciones[0], accion])
            self.estado_actual = accion

        self.estado_actual = self.analisis([token])

    def desplazar(self, token, accion):
        pila_str = ", ".join(map(str, self.pila))
        print("Entrada " + token + " pila: (" + pila_str + ") Desplaza " + token + " a la pila y estado:" + accion)

        self.pila.extend([token, accion])
        self.estado_actual = accion
        print("sig estado actual: " + self.estado_actual + " accion: " + accion)


# Uso del analizador sintáctico
analizador = AnalizadorSintactico()
tokens = ["token1", "token2", "token3"]  # Reemplaza con tus tokens reales
analizador.analisis(tokens)
