contador = 10
dispositivo = "Smart Things-d0:52:a8:00:67:5e-Wired"
dispositivo_coma = dispositivo.replace('-',';')
elementos = dispositivo_coma.split(';')

print("host" , elementos[0] , "{")
print("#asignaciono automatica")
print("hardware ethernet", elementos[1], ";#Direccion mac del host")
print("fixed-addres 192.168.0." + str(contador) + " ;#IP a asignar el host")
print("}")