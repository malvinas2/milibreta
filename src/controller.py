"""
controller.py:
    Controlador milibreta App
"""
__author__ = "Matthias Bergmann"
__email__ = "malvinas2@gmx.de"
__copyright__ = "Copyright 2025"
__versión__ = "2025-03-03"

from src import clases

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.solofichero = ''
        self.view.boton_alta.config(command=self.addDataToLbx)
        # self.view.boton_alta["command"] = self.addDataToLbx
        self.view.boton_modificar.config(command=self.updateDataFromLBX)
        self.view.boton_borrar.config(command=self.removeDataFromLBX)
        self.view.boton_reiniciar.config(command=self.clearEntry)
        self.view.boton_image.config(command=self.abreImagen)
        self.view.tree.bind('<<TreeviewSelect>>', self.loadDataToEntry)
        self.loadDataToLBX()

    def loadDataToLBX(self):
        data = self.model.getAllData()
        self.view.setListbox(data)

    def addDataToLbx(self):
        self.addToDB()
        self.loadDataToLBX()

    def removeDataFromLBX(self):
        self.removeDataFromDB()
        self.clearEntry()
        self.loadDataToLBX()

    def updateDataFromLBX(self):
        self.updateDB()
        self.loadDataToLBX()

    def loadDataToEntry(self, event=None):
        # id_ = self.view.getCursorID() or ''
        id_ = self.view.getCursorID()
        print("ID: ", id_)
        # print("ID: ", id_, "\nNOMBRE: ", nombre, "\nAPELLIDO: ", apellido)
        data = self.model.consultar(id_)
        print("data: ", data)
        nombre = data[0].nombre
        empresa = data[0].empresa
        calle = data[0].calle
        cp = data[0].cp
        telefono = data[0].telefono
        mail = data[0].mail
        apellido = data[0].apellido
        numero = data[0].numero
        ciudad = data[0].ciudad
        fax = data[0].fax
        solofichero = data[0].ruta
        self.solofichero = solofichero
        self.view.borrarTodo()
        self.view.setEntries(nombre, empresa, calle, cp, telefono, mail, apellido, numero, ciudad, fax, solofichero)

    def addToDB(self):
        nombre = self.view.getNombre()
        empresa = self.view.getEmpresa()
        calle = self.view.getCalle()
        cp = self.view.getCP()
        telefono = self.view.getTelefono()
        mail = self.view.getMail()
        apellido = self.view.getApellido()
        numero = self.view.getNumero()
        ciudad = self.view.getCiudad()
        fax = self.view.getFax()
        id_ = self.view.getCursorID()
        solofichero = self.solofichero
        try:
            self.model.addToTable(nombre, empresa, calle, cp, telefono, mail, apellido, numero, ciudad, fax, solofichero)
        except clases.EmailInvalido:
            self.view.showErrorMessage("Mensaje de error", "La dirección de email no es válida. Por favor corríjala. ")
        except clases.NombreApellidoVacio:
            self.view.showErrorMessage("Mensaje de error", "Los campos de 'Nombre' y 'Apellido' deben ser completados. Por favor corríjalo. ")

    def updateDB(self):
        nombre = self.view.getNombre()
        empresa = self.view.getEmpresa()
        calle = self.view.getCalle()
        cp = self.view.getCP()
        telefono = self.view.getTelefono()
        mail = self.view.getMail()
        apellido = self.view.getApellido()
        numero = self.view.getNumero()
        ciudad = self.view.getCiudad()
        fax = self.view.getFax()
        solofichero = self.solofichero
        id_ = self.view.getCursorID()
        try:
            self.model.updateTable(id_, nombre, empresa, calle, cp, telefono, mail, apellido, numero, ciudad, fax, solofichero)
        except clases.EmailInvalido:
            self.view.showErrorMessage("Mensaje de error", "La dirección de email no es válida. Por favor corríjala. ")
        except clases.NombreApellidoVacio:
            self.view.showErrorMessage("Mensaje de error", "Los campos de 'Nombre' y 'Apellido' deben ser completados. Por favor corríjalo. ")

    def removeDataFromDB(self):
        id_ = self.view.getCursorID()
        if id_:
            mensaje = "¿Estás seguro de eliminar la entrada de "
            mensaje = mensaje + self.view.getCursorNombre() + ' ' + self.view.getCursorApellido() + ' ?'
            if self.view.preguntaSiNo("Eliminar entrada", mensaje):
                self.model.deleteDataFromTable(id_)

    def abreImagen(self):
        self.solofichero = self.view.fileDialog()
        if self.solofichero != "":
            self.view.muestraImagen(self.solofichero)

    def clearEntry(self):
        self.solofichero = self.view.borrarTodo()
