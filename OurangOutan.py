import tkinter as tk
from tkinter import ttk
from Cameleon import *
from Faucon import *
class Lion(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Variable that are spreaded throughout the program
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        # Grid scaling
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        hyene = Hyene(self)
        hyene.grid(row=1, column=2)
        lionceau = Lionceau(self)
        lionceau.grid(row=1, column=0)
        fourmi = Fourmi(self)
        fourmi.grid(row=1, column=1)
        lionneQuiJuge = LionneQuiJuge(self)
        lionneQuiJuge.grid(row=0, column=2)
        lionneQuiRegarde = LionneQuiRegarde(self)
        lionneQuiRegarde.grid(row=0, column=0, columnspan=2)
        faucon= Faucon(lionceau, hyene.dictHyene,
                       lionneQuiJuge.course,
                       lionneQuiRegarde.vision,
                       fourmi)
        hyene.faucon = faucon
        hyene.une_hyene_est_nee()

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
        self.vision.axes.set_xlim(left=0, right=0.01)
        self.vision.axes.set_ylim(bottom=0, top=0.01)
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
        self.faucon = None

        # List complete de Hyene
        self.dictHyene = {}
        self.number=1
        # Creating combobox
        self.listHyene = ttk.Combobox(self, textvariable='',
                                 state='readonly')
        self.listHyene.grid(row=0, column=0, sticky='nsew')
        # Binding the click with frame switch
        self.listHyene.bind('<<ComboboxSelected>>', lambda e:
                       self.change_hyene(self.dictHyene, self.listHyene.get()))

        tempAjouter=tk.Button(self, text='Ajouter Hyene',
                          command=lambda:self.ajouter_hyene(self.listHyene,
                                                      self.number))
        tempAjouter.grid(column=0, row=2)
        destroyHyene=tk.Button(self, text='Destroy Hyene',
                          command=lambda:self.detruire_hyene(self.listHyene,
                                                            self.listHyene.get()))
        destroyHyene.grid(column=1, row=2)
        for i in range(1):
            for j in range(1):
                self.grid_columnconfigure(i, weight=1)
                self.grid_rowconfigure(j, weight=1)

        self.config(labelwidget=self.listHyene, width=100, height=100)

    def ajouter_hyene(self, Hyenes=None, numero=None):
        Hyenes['value'] = Hyenes['value'] + ('Hyene:'+
                                                 '{}'.format(numero), )
        self.dictHyene['Hyene:{}'.format(numero)] = BebeHyene(self, self.faucon)
        self.number+=1
        if self.faucon:
            self.faucon.dict_hyene_to_poulpe()

    def detruire_hyene(self, Hyenes, HyenesMourante):
        troupeHyene = list(Hyenes['value'])
        troupeHyene.remove(HyenesMourante)
        Hyenes['value'] = tuple(troupeHyene)
        Hyenes.current(0)
        self.change_hyene(self.dictHyene, Hyenes.get())
        del self.dictHyene[HyenesMourante]
        if self.faucon:
            self.faucon.dict_hyene_to_poulpe()

    def change_hyene(self, hyenes, nouvelhyene):
        for hyene in hyenes:
            hyenes[hyene].grid_forget()
        hyenes[nouvelhyene].grid(column=0, row=0, sticky='nsew',
                                    columnspan=2)
    def une_hyene_est_nee(self):
        self.listHyene['values'] = ['Hyene:0']
        self.dictHyene['Hyene:0'] = BebeHyene(self, self.faucon)
        self.listHyene.current(0)
        self.change_hyene(self.dictHyene, self.listHyene.get())
        self.faucon.dict_hyene_to_poulpe()

class BebeHyene(tk.Frame):
    def __init__(self, Hyene, faucon):
        tk.Frame.__init__(self, Hyene)
        positionX = tk.DoubleVar()
        positionY = tk.DoubleVar()
        self.force = tk.DoubleVar()
        self.force.set(1)
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
        if faucon:
            posXE.grid(row=0, column=1, sticky='nsew')
            posYE.grid(row=0, column=2, sticky='nsew')
            forceE.grid(row=2, column=1, sticky='nsew',
                        columnspan=2)
            posXE.bind('<Return>', lambda e:faucon.update_graphB())
            posYE.bind('<Return>', lambda e:faucon.update_graphB())
            forceE.bind('<Return>', lambda e:faucon.update_graphB())

        for i in range(2):
            self.grid_columnconfigure(i, weight=1)
            for j in range(2):
                self.grid_rowconfigure(j, weight=1)

if __name__ == '__main__':
    app = Lion()
    app.mainloop()
