nume = ["Ion","Bula","sile","cucu","GODAC","j&k","CORO"]

submultime = {element[0].upper() + element[1:].lower() for element in nume if len(element) > 2 and len(element) < 4}
print(list(submultime))

dictionar = {'a' : 10, 'b' : 34,'A' : 7,'Z' : 3}

frecv_dictionar = {k.lower() : dictionar.get(k.lower(),0) + dictionar.get(k.upper(),0) for k in dictionar.keys()}

print(frecv_dictionar)


import tkinter as tk
class Desen(tk.Canvas):
    def __init__(self,master = None):
        tk.Frame.__init__(self,master)
        self.w = 800
        self.h = 600
        self.master = master
        self.pack()
        self.desen = tk.Canvas(self.master,width = self.w,height = self.h)

        self.desen.create_line(0,0,self.w,self.h,fill="#FF0000",width = 3)
        self.desen.create_oval(10,10,100,100)
        self.desen.place(x = 0,y = 0)

root = tk.Tk()
root.geometry("800x500")
app = Desen(root)
app.mainloop()

