from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    matricula = IntegerField('Matricula',[
        validators.DataRequired(message="Este campo es requerido"),
        validators.NumberRange(min=100, max=1000, message="Ingrese un valor valido")
    ])
    nombre = StringField('Nombre',[
        validators.DataRequired(message="Este campo es requerido"),
        validators.length(min=3, max=10, message="Longitud de 3 a 10 caracteres")
    ])
    apaterno = StringField('Apaterno',[
        validators.DataRequired(message="Este campo es requerido")
    ])
    amaterno = StringField('Amaterno',[
        validators.DataRequired(message="Este campo es requerido")
    ])
    correo = EmailField('Correo',[
        validators.DataRequired(message="Este campo es requerido")
    ])