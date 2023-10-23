import sys
import lexico
import sintactico

keyword = ["int","char","float"]
cod_intermedio = []
estado_actual = "I0"
if len(sys.argv) == 2:
    archivo = sys.argv[1]
    if archivo.endswith(".ibi"):
        try:
            with open(archivo, "r") as file:
                for linea in file:
                    #linea = linea.split()
                    tokens = lexico.analisis(linea)
                    for token in tokens:
                        if token.type == "KeyWord":
                            cod_intermedio.append(token.value)
                        elif token.type == "Numero" or token.type == "Flotante":
                            cod_intermedio.append("num")
                        elif token.type == "Character" or token.type == "Id":
                            cod_intermedio.append("id")
                        elif token.type == "Symbol":
                            cod_intermedio.append(token.value)
                cod_intermedio = [item for item in cod_intermedio if item != ' ']
                cod_intermedio += "$"
                sintactico.analisis(cod_intermedio,estado_actual)  
        except lexico.CaracterNoReconocidoError as e:
            print(f"Error lexico : ",e)
        except FileNotFoundError:
            print(f"El archivo {archivo} no se encontro")
        except Exception as e:
            print(f"Ocurrio un error: {e}")
    else:
        print("Error el archivo no es de .ibi")
else :
    print("No se especifico el archivo a analizar")
