"""
view.py:
    Paquete de vista milibreta App.
"""


import os
from src import constants
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import *
from PIL import ImageTk, Image
from tkinter import filedialog


# ##############################################
# VISTA
# ##############################################

class View:
    def __init__(self, root):
        self.root = root
        self.root.title("Libreta de direcciones")
        # self.root.configure(background='grey') # master["bg"] = "black"
        # titulo = Label(root, text="Ingrese sus datos", bg="DarkOrchid3", fg="thistle1", height=1, width=60)
        # titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W + E)
        self.createWidgets()


    def createWidgets(self):
        self.addPicure = tk.PhotoImage(file=constants.ADD_PICTURE)
        self.boton_alta = ttk.Button(self.root, width=10, text="Alta", image=self.addPicure, compound='left')
        self.boton_alta.grid(row=1, column=2, sticky='ew')

        self.resetPicture = tk.PhotoImage(file=constants.RESET_PICTURE)
        self.boton_reiniciar = ttk.Button(self.root, width=10, text="Reiniciar", image=self.resetPicture, compound='left')
        self.boton_reiniciar.grid(row=3, column=2, sticky='ew')

        self.deletePicture = tk.PhotoImage(file=constants.DELETE_PICTURE)
        self.boton_borrar = ttk.Button(self.root, width=10, text="Borrar", image=self.deletePicture, compound='left')
        self.boton_borrar.grid(row=5, column=2, sticky='ew')

        self.updatePicture = tk.PhotoImage(file=constants.UPDATE_PICTURE)
        self.boton_modificar = ttk.Button(self.root, width=10, text="Modificar", image=self.updatePicture, compound='left')
        self.boton_modificar.grid(row=7, column=2, sticky='ew')

        self.lblNombre = ttk.Label(self.root, text="Nombre")
        self.lblNombre.grid(row=1, column=6, sticky='w')
        self.lblEmpresa = ttk.Label(self.root, text="Empresa")
        self.lblEmpresa.grid(row=2, column=6, sticky='w')
        self.lblCalle = ttk.Label(self.root, text="Calle")
        self.lblCalle.grid(row=3, column=6, sticky='w')
        self.lblCP = ttk.Label(self.root, text="CP")
        self.lblCP.grid(row=4, column=6, sticky='w')
        self.lblTelefono = ttk.Label(self.root, text="Teléfono")
        self.lblTelefono.grid(row=5, column=6, sticky='w')
        self.lblMail = ttk.Label(self.root, text="Correo electrónico")
        self.lblMail.grid(row=6, column=6, sticky='w')

        self.lblApellido = ttk.Label(self.root, text="Apellido")
        self.lblApellido.grid(row=1, column=9, sticky='w')
        self.lblNumero = ttk.Label(self.root, text="N°")
        self.lblNumero.grid(row=3, column=9, sticky='w')
        self.lblCiudad = ttk.Label(self.root, text="Ciudad")
        self.lblCiudad.grid(row=4, column=9, sticky='w')
        self.lblFax = ttk.Label(self.root, text="Fax")
        self.lblFax.grid(row=5, column=9, sticky='w')

        # Defino variables para tomar valores de campos de entrada
        w_ancho = 15

        self.entryNombreTextVar = tk.StringVar()
        self.entryNombre = ttk.Entry(self.root, textvariable=self.entryNombreTextVar, width=w_ancho)
        self.entryNombre.grid(row=1, column=7, sticky='w')
        self.entryEmpresaTextVar = tk.StringVar()
        self.entryEmpresa = ttk.Entry(self.root, textvariable=self.entryEmpresaTextVar, width=int(2.8*w_ancho))
        self.entryEmpresa.grid(row=2, column=7, columnspan=4, sticky='w')
        self.entryCalleTextVar = tk.StringVar()
        self.entryCalle = ttk.Entry(self.root, textvariable=self.entryCalleTextVar, width=w_ancho)
        self.entryCalle.grid(row=3, column=7, sticky='w')
        self.entryCPTextVar = tk.StringVar()
        self.entryCP = ttk.Entry(self.root, textvariable=self.entryCPTextVar, width=w_ancho)
        self.entryCP.grid(row=4, column=7, sticky='w')
        self.entryTelefonoTextVar = tk.StringVar()
        self.entryTelefono = ttk.Entry(self.root, textvariable=self.entryTelefonoTextVar, width=w_ancho)
        self.entryTelefono.grid(row=5, column=7, sticky='w')
        self.entryMailTextVar = tk.StringVar()
        self.entryMail = ttk.Entry(self.root, textvariable=self.entryMailTextVar, width=int(2.8*w_ancho))
        self.entryMail.grid(row=6, column=7, columnspan=4, sticky='w')

        self.entryApellidoTextVar = tk.StringVar()
        self.entryApellido = ttk.Entry(self.root, textvariable=self.entryApellidoTextVar, width=w_ancho)
        self.entryApellido.grid(row=1, column=10, sticky='w')
        self.entryNumeroIntVar = tk.IntVar()
        self.entryNumero = ttk.Entry(self.root, textvariable=self.entryNumeroIntVar, width=w_ancho)
        self.entryNumero.grid(row=3, column=10, sticky='w')
        self.entryCiudadTextVar = tk.StringVar()
        self.entryCiudad = ttk.Entry(self.root, textvariable=self.entryCiudadTextVar, width=w_ancho)
        self.entryCiudad.grid(row=4, column=10, sticky='w')
        self.entryFaxTextVar = tk.StringVar()
        self.entryFax = ttk.Entry(self.root, textvariable=self.entryFaxTextVar, width=w_ancho)
        self.entryFax.grid(row=5, column=10, sticky='w')

        # space holder, just for design purposes
        self.spacer2 = ttk.Label(self.root, text="")
        self.spacer2.grid(row=1, column=11)

        self.ruta_val = tk.StringVar()

        self.boton_image = ttk.Button(self.root, width=10, text="Imagen")
        self.boton_image.grid(row=8, column=6, sticky='w')
        self.panel = ttk.Label(self.root)
        self.panel.grid(row=9, column=7, columnspan=4, rowspan=3)

        # --------------------------------------------------
        # TREEVIEW
        # --------------------------------------------------

        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("col1", "col2")
        self.tree.column("#0", width=90, minwidth=50, anchor='w')
        self.tree.column("col1", width=150, minwidth=80)
        self.tree.column("col2", width=150, minwidth=80)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Nombre")
        self.tree.heading("col2", text="Apellido")
        self.tree.grid(row=9, column=1, columnspan=3, rowspan=6)
        self.spacer1 = ttk.Label(self.root, text="")
        self.spacer1.grid(row=15, column=1)

        self.scrollbar = ttk.Scrollbar(self.root)
        self.scrollbar.grid(row=9, column=5, rowspan=6, sticky='ns')

        self.scrollbar.configure(command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # style
        tree_style = ttk.Style()       # ##### porque no se usa 'self' aca ?  self.tree_style ....
        tree_style.theme_use('winnative')
        # tree_style.configure('Treeview.Heading', background="darksalmon")

        # spacing on columns/rows in the grid
        # https://stackoverflow.com/questions/28019402/tkinter-grid-spacing-options
        col_count, row_count = self.root.grid_size()
        for col in range(col_count):
            self.root.grid_columnconfigure(col, minsize=10)
        for row in range(row_count):
            self.root.grid_rowconfigure(row, minsize=10)

    def getNombre(self):
        return self.entryNombreTextVar.get()

    def getEmpresa(self):
        return self.entryEmpresaTextVar.get()

    def getCalle(self):
        return self.entryCalleTextVar.get()

    def getCP(self):
        return self.entryCPTextVar.get()

    def getTelefono(self):
        return self.entryTelefonoTextVar.get()

    def getMail(self):
        return self.entryMailTextVar.get()

    def getApellido(self):
        return self.entryApellidoTextVar.get()

    def getNumero(self):
        try:
            numero = self.entryNumeroIntVar.get()
        except Exception:
            self.setNumero(0)
            return 0
        else:
            return numero

    def getCiudad(self):
        return self.entryCiudadTextVar.get()

    def getFax(self):
        return self.entryFaxTextVar.get()

    def setNombre(self, nombre):
        return self.entryNombreTextVar.set(nombre)

    def setEmpresa(self, empresa):
        return self.entryEmpresaTextVar.set(empresa)

    def setCalle(self, calle):
        return self.entryCalleTextVar.set(calle)

    def setCP(self, cp):
        return self.entryCPTextVar.set(cp)

    def setTelefono(self, telefono):
        return self.entryTelefonoTextVar.set(telefono)

    def setMail(self, mail):
        return self.entryMailTextVar.set(mail)

    def setApellido(self, apellido):
        return self.entryApellidoTextVar.set(apellido)

    def setNumero(self, numero):
        return self.entryNumeroIntVar.set(numero)

    def setCiudad(self, ciudad):
        return self.entryCiudadTextVar.set(ciudad)

    def setFax(self, fax):
        return self.entryFaxTextVar.set(fax)

    def getTreeviewSelection(self):
        selections = self.tree.selection()
        if selections:
            selection = selections[0]
            # values = self.treeview.item(selection)['values']
            values = self.tree.item(selection, "values")
            return values
            # https://stackoverflow.com/questions/30614279/tkinter-treeview-get-selected-item-values
            # tree.item outputs a dictionary, from which one can then retrieve individual values:
            # {'text': 'Name', 'image': '', 'values': [u'Date', u'Time', u'Loc'], 'open': 0, 'tags': ''}
            # ttk.treeview.focus() returns the current focus item. That means the item that was last selected.
            # ttk.treeview.selection() returns a tuple of all the selected items.
        return None

    def getCursorID(self, event=None):
        valor = self.tree.selection()
        if valor:
            print(valor)  # ('I005',)
            item = self.tree.item(valor)
            print(item)  # {'text': 5, 'image': '', 'values': ['daSDasd', '13.0', '2.0'], 'open': 0, 'tags': ''}
            print(item['text'])
            mi_id = item['text']
            return mi_id
        return None

    def getCursorNombre(self):
        selectedData = self.getTreeviewSelection()
        if selectedData:
            return selectedData[0]
        return None

    def getCursorApellido(self):
        selectedData = self.getTreeviewSelection()
        if selectedData:
            return selectedData[1]
        return None

    def setListbox(self, data):
        self.tree.delete(*self.tree.get_children())
        # for item in self.tree.get_children():  # used self.tree instead
        #    self.tree.delete(item)
        for values in data:
            # self.tree.insert('', 'end', values=(values))
            # self.tree.insert("", 0, text=values[0], values=(values[1], values[7]))
            self.tree.insert("", 0, text=values.id, values=(values.nombre, values.apellido))

    def borrarTodo(self):
        self.setNombre("")
        self.setEmpresa("")
        self.setCalle("")
        self.setCP("")
        self.setTelefono("")
        self.setMail("")
        self.setApellido("")
        self.setNumero(0)
        self.setCiudad("")
        self.setFax("")

        self.panel.image = None
        self.muestraImagen(constants.DEFAULT_PROFILE)
        return constants.DEFAULT_PROFILE

    def setEntries(self, nombre, empresa, calle, cp, telefono, mail, apellido, numero, ciudad, fax, image):
        self.setNombre(nombre)
        self.setEmpresa(empresa)
        self.setCalle(calle)
        self.setCP(cp)
        self.setTelefono(telefono)
        self.setMail(mail)
        self.setApellido(apellido)
        self.setNumero(numero)
        self.setCiudad(ciudad)
        self.setFax(fax)
        self.muestraImagen(image)

    def fileDialog(self):
        rutayfichero = tk.filedialog.askopenfilename(initialdir=constants.PICTURES_DIR, title='open')
        solofichero = os.path.basename(rutayfichero)
        print(rutayfichero)
        print(solofichero)
        return solofichero

    def muestraImagen(self, imagen):
        rutayfichero = os.path.join(constants.PICTURES_DIR, imagen)
        print("view.muestraImagen 1: ", rutayfichero)
        print("view.muestraImagen 2: ", os.path.basename(rutayfichero))
        try:
            img = Image.open(rutayfichero)
        except PermissionError:
            pass
        print("view.muestraImagen 3: ", img)
        # img = ImageTk.PhotoImage(Image.open('download.gif'))
        width, height = img.size
        ratio = width / height
        # https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
        new_width = 250
        new_height = int(new_width / ratio)
        img = img.resize((new_width, new_height))
        print(img)
        img = ImageTk.PhotoImage(img)
        print(img)
        # panel = Label(root, image=img)
        print(self.panel)
        self.panel.config(image=img)
        self.panel.image = img
        # panel.grid(row=9, column=7, columnspan=4, rowspan=3)

    def showErrorMessage(self, title, mensaje):
        showerror(title, mensaje)

    def preguntaSiNo(self, title, mensaje):
        # mensaje = mensaje + self.getCursorNombre() + ' ' + self.getCursorApellido() + ' ?'
        if askyesno(title, mensaje):
            return 1
        else:
            return 0
