import tkinter as tk
from tkinter import ttk
from Cameleon import *

class Lion(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Variable that are spreaded throughout the program
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        # Grid scaling
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        Hyene(self).grid(row=1, column=2)
        Lionceau(self).grid(row=1, column=0)
        Fourmi(self).grid(row=1, column=1)
        LionneQuiJuge(self).grid(row=0, column=2)
        LionneQuiRegarde(self).grid(row=0, column=0, columnspan=2)

        for i in range(2):
            self.grid_columnconfigure(i, weight=1)
            for j in range(2):
                self.grid_rowconfigure(j, weight=1)

    def frame_switch(self, dict_, new):
        for frame in self.Frame:
            frame.grid_forget()
        new.grid(column=1, row=1, sticky='nsew')

class LionneQuiJuge(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.course = Cameleon(self, axis_name=['', ''], figsize=[2, 2])
        self.bind('<Configure>', self.course.change_dimensions)

        for i in range(2):
            self.grid_columnconfigure(i, weight=1)
            for j in range(2):
                self.grid_rowconfigure(j, weight=1)

class LionneQuiRegarde(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.vision = Cameleon(self, axis_name=['', ''], figsize=[4, 4])
        self.bind('<Configure>', self.vision.change_dimensions)
        for i in range(2):
            self.grid_columnconfigure(i, weight=1)
            for j in range(2):
                self.grid_rowconfigure(j, weight=1)

class Lionceau(ttk.LabelFrame):
    def __init__(self, parent):
        ttk.LabelFrame.__init__(self, parent, text='Lionceau')
        vitesseX = tk.DoubleVar()
        vitesseY = tk.DoubleVar()
        positionX = tk.DoubleVar()
        positionY = tk.DoubleVar()
        self.force = tk.DoubleVar()
        self.pos = [positionX, positionY]
        self.vit = [vitesseX, vitesseY]

        tk.Label(self, text='Position [X,Y] :').grid(row=0, column=0,
                                                     sticky='nw')
        tk.Label(self, text='Vitesse [X,Y] :').grid(row=1, column=0,
                                                   sticky='nw')
        tk.Label(self, text='Force :').grid(row=2, column=0,
                                                   sticky='nw')
        posXE = tk.Entry(self, textvariable=positionX,
                        width=6)
        posYE = tk.Entry(self, textvariable=positionY,
                        width=6)
        vitXE = tk.Entry(self, textvariable=vitesseX,
                        width=6)
        vitYE = tk.Entry(self, textvariable=vitesseY,
                        width=6)
        forceE = tk.Entry(self, textvariable=self.force,
                        width=6)

        posXE.grid(row=0, column=1, sticky='nsew')
        posYE.grid(row=0, column=2, sticky='nsew')
        vitXE.grid(row=1, column=1, sticky='nsew')
        vitYE.grid(row=1, column=2, sticky='nsew')
        forceE.grid(row=2, column=1, sticky='nsew',
                   columnspan=2)

        for i in range(2):
            self.grid_columnconfigure(i, weight=1)
            for j in range(2):
                self.grid_rowconfigure(j, weight=1)

class Fourmi(ttk.LabelFrame):
    def __init__(self, parent):
        ttk.LabelFrame.__init__(self, parent, text='Fourmi')
        self.dq = tk.DoubleVar()
        self.nt = tk.IntVar()
        self.dt = tk.DoubleVar()

        tk.Label(self, text='\u03B4'+'q :').grid(row=0, column=0,
                                                     sticky='nw')
        tk.Label(self, text='\u03B4'+'t :').grid(row=1, column=0,
                                                   sticky='nw')
        tk.Label(self, text='nt:').grid(row=2, column=0,
                                                   sticky='nw')
        dqE = tk.Entry(self, textvariable=self.dq,
                        width=6)
        dtE = tk.Entry(self, textvariable=self.dt,
                        width=6)
        dntE = tk.Entry(self, textvariable=self.nt,
                        width=6)

        dqE.grid(row=0, column=1, sticky='nsew')
        dtE.grid(row=1, column=1, sticky='nsew')
        dntE.grid(row=2, column=1, sticky='nsew')

        for i in range(2):
            self.grid_columnconfigure(i, weight=1)
            for j in range(2):
                self.grid_rowconfigure(j, weight=1)

class Hyene(ttk.LabelFrame):
    def __init__(self, parent):
        ttk.LabelFrame.__init__(self, parent)


        # List complete de Hyene
        self.dictHyene = {}
        self.number=1
        # Creating combobox
        listHyene = ttk.Combobox(self, textvariable='',
                                 state='readonly')
        listHyene.grid(row=0, column=0, sticky='nsew')
        # Binding the click with frame switch
        listHyene.bind('<<ComboboxSelected>>', lambda e:
                       self.change_hyene(self.dictHyene, listHyene.get()))

        listHyene['values'] = ['Hyene:0']
        self.dictHyene['Hyene:0'] = BebeHyene(self)
        listHyene.current(0)
        self.change_hyene(self.dictHyene, listHyene.get())
        tempAjouter=tk.Button(self, text='Ajouter Hyene',
                          command=lambda:self.ajouter_hyene(listHyene,
                                                      self.number))
        tempAjouter.grid(column=0, row=2)
        destroyHyene=tk.Button(self, text='Destroy Hyene',
                          command=lambda:self.detruire_hyene(listHyene,
                                                            listHyene.get()))
        destroyHyene.grid(column=1, row=2)
        for i in range(1):
            for j in range(1):
                self.grid_columnconfigure(i, weight=1)
                self.grid_rowconfigure(j, weight=1)

        self.config(labelwidget=listHyene, width=100, height=100)

    def ajouter_hyene(self, Hyenes, numero):
        Hyenes['value'] = Hyenes['value'] + ('Hyene:'+
                                                 '{}'.format(numero), )
        self.dictHyene['Hyene:{}'.format(numero)] = BebeHyene(self)
        self.number+=1

    def detruire_hyene(self, Hyenes, HyenesMourante):
        troupeHyene = list(Hyenes['value'])
        troupeHyene.remove(HyenesMourante)
        Hyenes['value'] = tuple(troupeHyene)
        Hyenes.current(0)
        self.change_hyene(self.dictHyene, Hyenes.get())
        del self.dictHyene[HyenesMourante]

    def change_hyene(self, hyenes, nouvelhyene):
        for hyene in hyenes:
            hyenes[hyene].grid_forget()
        hyenes[nouvelhyene].grid(column=0, row=0, sticky='nsew',
                                    columnspan=2)

class BebeHyene(tk.Frame):
    def __init__(self, Hyene):
        tk.Frame.__init__(self, Hyene)
        positionX = tk.DoubleVar()
        positionY = tk.DoubleVar()
        self.force = tk.DoubleVar()
        self.pos = [positionX, positionY]

        tk.Label(self, text='Position [X,Y] :').grid(row=0, column=0,
                                                     sticky='nw')
        tk.Label(self, text='Force :').grid(row=2, column=0,
                                                   sticky='nw')
        posXE = tk.Entry(self, textvariable=positionX,
                        width=6)
        posYE = tk.Entry(self, textvariable=positionY,
                        width=6)
        forceE = tk.Entry(self, textvariable=self.force,
                        width=6)

        posXE.grid(row=0, column=1, sticky='nsew')
        posYE.grid(row=0, column=2, sticky='nsew')
        forceE.grid(row=2, column=1, sticky='nsew',
                   columnspan=2)

        for i in range(2):
            self.grid_columnconfigure(i, weight=1)
            for j in range(2):
                self.grid_rowconfigure(j, weight=1)

if __name__ == '__main__':
    app = Lion()
    app.mainloop()
