from tkinter import*

class WindowInvit(object):
   def __init__(self, geometry = None):
       
       self.root = Tk()
       self.root.geometry(geometry)
       self.root['bg'] = '#696969'
       self.root.resizable(width=False, height=False)
       self.root.title('Apps')

       self.FraBut = Frame(self.root, bg = '#778899')
       self.FraBut.place(x=80, y=85)

       self.ButCreatRec = Button(self.FraBut, text='CREAT', height=1, width=15, bg = '#778899', font = ('Times', 10), fg = '#000000')
       self.ButCreatRec.pack()

       self.ButInRec = Button(self.FraBut, text='INOUT', height=1, width=15, bg = '#778899', font = ('Times', 10), fg = '#000000')
       self.ButInRec.pack()

       self.LogEnt = Entry(self.root, width=40, font = ('Times', 10))
       self.LogEnt.place(x=10, y=15)
       self.PasEnt = Entry(self.root, width=40, font = ('Times', 10))
       self.PasEnt.place(x=10, y=50)

       self.root.mainloop()

app = WindowInvit('280x160')