"""
model.py:
    modelo milibreta App
"""
__author__ = "Matthias Bergmann"
__email__ = "malvinas2@gmx.de"
__copyright__ = "Copyright 2025"
__versión__ = "2025-03-03"

import re
import peewee
from src import constants
from src import clases

db = peewee.SqliteDatabase(constants.DATABASE_NAME)


class BaseModel(peewee.Model):
    class Meta:
        """
        Creación Base de Datos.

        :param db: database.
        """
        database = db


class Libreto(BaseModel):
    """
    Creación de tabla: Libreto.
    Tipos de datos para cada campo en la tabla.
    """
    id = peewee.IntegerField(primary_key=True)
    nombre = peewee.CharField()
    empresa = peewee.CharField()
    calle = peewee.CharField()
    cp = peewee.CharField()
    telefono = peewee.CharField()
    mail = peewee.CharField()
    apellido = peewee.CharField()
    numero = peewee.IntegerField()
    ciudad = peewee.CharField()
    fax = peewee.CharField()
    ruta = peewee.CharField()

    class Meta:
        table_name = 'libreto'


db.connect()

try:
    db.create_tables([Libreto])
except peewee.OperationalError:
    print("Tabla ya existe")


class Model:

    # ##############################################
    # MODELO ABMC
    # ##############################################

    def __init__(self):
        pass

    def isValid(self, regex, entry):
        if re.fullmatch(regex, entry) or entry == '':
            return True
        else:
            return False

    def consultar(self, index):
        """
        Método para recuperar los detalles de contacto de la entrada seleccionada de la base de datos

        :param links: index
        """
        print("consultar")
        query = list(Libreto.select().where(Libreto.id == index))
        print(query)
        return query

    def getAllData(self):
        """
        Método para obtener todos los nombres de la base de datos.

        """
        resultado = Libreto.select()
        # resultado = list(Libreto.select())

        # query = Libreto.select(Libreto.nombre, Libreto.calle)
        # print(query)
        # print(query[3].nombre)
        # for libreto in query:
        #     print(libreto.nombre)
        # print("datenbankinhalt: ")

        print(resultado)
        return resultado

    def addToTable(self, nombre, empresa, calle, cp, telefono, mail, apellido, numero, ciudad, fax, solofichero):
        """
        Método para anadir datos en el registro seleccionado.

        :param links: id_, nombre, empresa, calle, cp, telefono, mail, apellido, numero, ciudad, fax, solofichero.
        """
        if self.isValid(constants.REGEX_MAIL, mail) is False:
            raise clases.EmailInvalido('Email vacio')
        if nombre == '' or apellido == '':
            raise clases.NombreApellidoVacio('Nobmre vacio')
        print(nombre, empresa, calle, cp, telefono, mail, apellido, numero, ciudad, fax, solofichero)
        nuevo_entrada = Libreto.insert(nombre=nombre, empresa=empresa, calle=calle, cp=cp, telefono=telefono, mail=mail, apellido=apellido, numero=numero, ciudad=ciudad, fax=fax, ruta=solofichero)
        nuevo_entrada.execute()
        print("Estoy en alta todo ok")

    def updateTable(self, id_, nombre, empresa, calle, cp, telefono, mail, apellido, numero, ciudad, fax, solofichero):
        """
        Método de modificación de datos en el registro seleccionado.

        :param links: id_, nombre, empresa, calle, cp, telefono, mail, apellido, numero, ciudad, fax, solofichero.
        """
        if self.isValid(constants.REGEX_MAIL, mail) is False:
            raise clases.EmailInvalido('Email vacio')
        if nombre == '' or apellido == '':
            raise clases.NombreApellidoVacio('Nobmre vacio')
        actualizar = Libreto.update(nombre=nombre, empresa=empresa, calle=calle, cp=cp, telefono=telefono, mail=mail, apellido=apellido, numero=numero, ciudad=ciudad, fax=fax, ruta=solofichero).where(Libreto.id == id_)
        actualizar.execute()

    def deleteDataFromTable(self, id_):
        """
        Método de eliminación de registros.

        :param item: id_.
        """
        query = Libreto.get(Libreto.id == id_)
        query.delete_instance()
