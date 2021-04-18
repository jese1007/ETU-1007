from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from Control_Ip import Control_Ip
import math

class Affichage(object):

    def Table(self,fenetre, titre, donnees):
        self.table.destroy()
        self.table = ttk.Treeview(fenetre)
        self.table['columns'] = titre
        self.table['show'] = 'headings'
        for i in range(len(titre)):
            self.table.column(""+titre[i], width=int(len(donnees[0][0])*6), anchor=CENTER)
            self.table.heading(""+titre[i], text=""+titre[i], anchor=CENTER)
        for y in range(len(donnees)):
            self.table.insert('', 'end', text="", values=donnees[y])
        self.table.place(x=10, y=50)

    def nbreAdresse(self,classe):
        return int(math.pow(2, 32-int(classe)))-2

    def listener(self):
        ip = self.entre.get()
        control = Control_Ip(str(ip))
        data = []
        if len(ip.split(":")) == 1:
            data.append(control.configIp4())
        elif len(ip.split(":")) > 1:
            data.append(control.configIp6())
        titre = data[0][0]
        donnees = [data[0][1]]
        self.Table(self.mainapp, titre, donnees)

    def __init__(self):
        self.mainapp = Tk()
        self.mainapp.title("IPV4 AVEC CLASSE ou IPV6 avec Abreviation")
        self.mainapp.geometry("1200x600")
        style = Style()
        style.configure('TButton', font=('Calibri',10,'bold'),foreground='blue')
        label = Label(self.mainapp, text="IP :", font=("Arial", 12))
        label.place(x=10, y=10, anchor=NW)
        self.entre = Entry(self.mainapp, font=("Arial", 10))
        self.entre.place(x=50, y=10, width=300)
        bouton = Button(self.mainapp, text="Valider", style='TButton', command=self.listener)
        bouton.place(x=400, y=10)
        self.table = ttk.Treeview(self.mainapp)
        self.table.place(x=10, y=50)
        self.mainapp.mainloop()
