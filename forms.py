from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField
from wtforms.fields import EmailField
from wtforms import validators


def mi_Validacion(form, field):
    if len(field.data) == 0:
        raise validators.ValidationError('El campo no tiene datos')


class UserForm(Form):
    matricula = StringField('Matricula', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=10, message='long de campo 4 min and 5 max')])
    nombre = StringField('Nombre', [
        validators.DataRequired(message='El campo es requerido')])
    apaterno = StringField('Apaterno', [mi_Validacion])
    amaterno = StringField('Amaterno')
    email = EmailField('Email')


class NumeroForm(Form):
    numero = StringField('Numero')


class LoginForm(Form):
    username = StringField('usuario', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=15, message='No cumple la longitud para el campo')
    ])
    password = StringField('password', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=15, message='No cumple la longitud para el campo')
    ])


class TraductorForm(FlaskForm):
    palabra = StringField('Palabra', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=15, message='No cumple la longitud para el campo')
    ])
    traduccion = StringField('Traduccion', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=2, max=15, message='No cumple la longitud para el campo')
    ])
    idioma = SelectField('Idioma', choices=[('1', 'Español - Ingles'), ('2', 'English - Spanish')], default='1')
    submit = SubmitField('Guardar')


class BuscadorForm(FlaskForm):
    palabra = StringField('Palabra', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=2, max=15, message='No cumple la longitud para el campo')
    ])
    idioma = SelectField('Idioma', choices=[('1', 'Español - Ingles'), ('2', 'English - Spanish')], default='1')
    submit = SubmitField('Guardar')


class ResistenciaForm(FlaskForm):
    banda1 = SelectField('Banda 1', choices=[('1', 'Negro'), 
                                                  ('2', 'Marron'), 
                                                  ('3', 'Rojo'), 
                                                  ('4', 'Naranja'), 
                                                  ('5', 'Amarillo'), 
                                                  ('6', 'Verde'), 
                                                  ('7', 'Azul'), 
                                                  ('8', 'Violeta'), 
                                                  ('9', 'Gris'), 
                                                  ('10', 'Blanco')], 
                              default='1')
    banda2 = SelectField('Banda 2', choices=[('1', 'Negro'), 
                                                  ('2', 'Marron'), 
                                                  ('3', 'Rojo'), 
                                                  ('4', 'Naranja'), 
                                                  ('5', 'Amarillo'), 
                                                  ('6', 'Verde'), 
                                                  ('7', 'Azul'), 
                                                  ('8', 'Violeta'), 
                                                  ('9', 'Gris'), 
                                                  ('10', 'Blanco')], 
                              default='1')
    banda3 = SelectField('Banda 3', choices=[('1', 'Negro'), 
                                                  ('2', 'Marron'), 
                                                  ('3', 'Rojo'), 
                                                  ('4', 'Naranja'), 
                                                  ('5', 'Amarillo'), 
                                                  ('6', 'Verde'), 
                                                  ('7', 'Azul'), 
                                                  ('8', 'Violeta'), 
                                                  ('9', 'Gris'), 
                                                  ('10', 'Blanco')], 
                              default='1')
    banda4 = SelectField('Banda 4', choices=[('1', 'Negro'), 
                                                  ('2', 'Marron'), 
                                                  ('3', 'Rojo'), 
                                                  ('4', 'Naranja'), 
                                                  ('5', 'Amarillo'), 
                                                  ('6', 'Verde'), 
                                                  ('7', 'Azul'), 
                                                  ('8', 'Violeta'), 
                                                  ('9', 'Gris'), 
                                                  ('10', 'Blanco')], 
                              default='1')
    tolerancia = RadioField('Tolerancia', choices=[('1', 'Dorado = 5%'), ('2', 'Plateado = 10%')], default='1')
    submit = SubmitField('Calcular')

