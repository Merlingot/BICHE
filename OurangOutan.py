import tkinter as tk
from tkinter import ttk

class Lion(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Variable that are spreaded throughout the program
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        # Grid scaling
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        Hyene(self).grid(row=0, column=0)
        Lionceau(self).grid(row=0, column=0)

    def frame_switch(self, dict_, new):
        for frame in self.Frame:
            frame.grid_forget()
        new.grid(column=1, row=1, sticky='nsew')

class Lionceau(ttk.LabelFrame):
    def __init__(self, parent):
        ttk.LabelFrame.__init__(self, parent, text='Lionceau')
        vitesseX = tk.StringVar()
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
        largeurHyene = tk.DoubleVar()
        largeurHyeneE = tk.Entry(self)
        hauteurHyene = tk.DoubleVar()
        hauteurHyeneE = tk.Entry(self)

        largeurHyeneE.grid(column=0, row=0)
        hauteurHyeneE.grid(column=1, row=0)

if __name__ == '__main__':
    app = Lion()
    app.mainloop()
