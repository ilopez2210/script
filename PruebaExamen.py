#SCRIPT parra crear un fichero .htacces

import sys
import os

if len(sys.argv) != 6:
    print("Necesita mas de 6 argumentos")
    sys.exit(1)
else:
#Crear el fichero htpasswd y escribir el argumento 3 y 4
    f = open(sys.argv[1]+'.htpasswd','w')
    f.write(f"{sys.argv[3]}:{sys.argv[4]}")
#Crear el fichero htaccess
    f = open(sys.argv[1]+'.htaccess','w')
    f.write("DirectoryIndex "+sys.argv[2]+'\n')
    f.write("AuthName \"Dialog prompt\"\n")
    f.write("AuthType Basic \n")
    f.write(sys.argv[1]+ "\.htpasswd\n")
#Opciones
    if sys.argv[5] == 'S':
        f.write("Options -Indexes\n")