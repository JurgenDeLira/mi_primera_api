from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

#
db = SQLAlchemy()

#Creamos una clase llamada "jwt" que nos ayuda a manejar todos los tokens que pasen por nuestra API
jwt = JWTManager()