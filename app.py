#Este archivoo se va a encargar de poner a correr el servidor

#Aqui solamente se va a ejecutar el comando necesario para ponerlo a correr
#__init__ significa inicializador
from app import configurar_app #con app se refiere a la carpeta, y est agarrando el model.py

#port -> Puerta, le estamos dando permiso a un usuario de conectarse
#22 -> ssh
#443 -> https
#80 (8080) -> http
#23 -> telnet
configurar_app().run(port=8080) 