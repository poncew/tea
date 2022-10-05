try:
 entrada = input("Ingrese el nombre del archivo: ")
 archivo = open(entrada, "r", encoding="UTF-8")
 for Línea in archivo:
  print(Línea.upper())
except:
    print("Error, archivo no existe")
