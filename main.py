from tkinter import *

from src import controller
from src import model
from src import view


if __name__ == '__main__':
    root = Tk()
    view = view.View(root)
    model = model.Model()
    controller = controller.Controller(model, view)
    root.mainloop()
