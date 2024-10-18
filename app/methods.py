# Ejecuta todas las peticiones que se hagan a la base datos


from app.models.usuarios import User
from flask_jwt_extended import create_access_token

from datetime import timedelta

def user_register(nombre, email, telefono, password):
  
  #Buscar si el correo del usuario ya esta registrado
  usuario_existente = User.query.filter_by(email=email).first()

  print(usuario_existente)

  if usuario_existente is not None:
    return {'Error': 'El usuario ya está registrado :('}, 403

  # Creamos un objeto de tipo User con los valores que el cliente solicitó
  nuevo_usuario = User(nombre=nombre, email=email, telefono=telefono)

  # Este método lo que hace es recibir la pass en texto plano, hashearla y guardarla dentro 
  # de nuestro objeto
  nuevo_usuario.hashear_password(password=password)

  # Invocamos el método Save que se encargar de hacer todo el proceso para
  # guardarlo en mi DB
  nuevo_usuario.save()

  return {
    'status': 'Usuario registrado',
    'email': email,
    'telefono': telefono
  }, 200


  #Esta función se encarga de hacer el login en nuestra API
def user_login(correo, password):

    #Tenemos que verificar que el usuario al que se esta intentando logger, existe

    #En mi BD se va buscar por el correo que el cliente haya mandado
    usuario_existente = User.query.filter_by(email=correo).first()

    #Esta condicional determina si mi usuario está registrado en la DB
    if usuario_existente is None:
        return {'Status': 'El correo no está registrado :( '}, 500
    
    #Verificamos que la contraseña coincida con la que está en la DB (True o False)
    elif usuario_existente.verificar_password(password = password):
        
        caducidad = timedelta(minutes=2)
        
        #Le creamos un token de acceso
        token_acceso = create_access_token(identity=usuario_existente.nombre, expires_delta=caducidad)

        return {
           'Status': 'Sesion iniciada',
           'Token': token_acceso
           }, 200

    #Si no coincide, le arrojamos un error al usuario 
    else:
        return{'Status': 'La contraseña no coincide :('}, 400

