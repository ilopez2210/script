import sys

if len(sys.argv) !=4:
    print("Se necesita 4 argumentos")
    sys.exit(1)

id_contenedor = sys.argv[1]
nombre_contendor = sys.argv[2]
descripcion_contendor = sys.argv[3]

fichero = open('contenedores.txt', 'r')
print (len(fichero.readlines()))

if len(fichero.readlines()) < 5:
    contenedores = open('contenedores.txt', 'a')
    contenedores.write(f"{id_contenedor} , {nombre_contendor}, {descripcion_contendor}\n")

else:
    