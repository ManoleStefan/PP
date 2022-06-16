from tkinter import *
import tkinter as tk

class LanguageFactory:
    def createButton(self):
        pass

class EnglishFactory(LanguageFactory):
    def createButton(self):
        b = Button(text="English")
        return b

class SpanishFactory(LanguageFactory):
    def createButton(self):
        b = tk.Button(text="Spanish")
        return b

class JapanesseFactory(LanguageFactory):
    def createButton(self):
        b = Button(text="Japanesse")
        return b

if __name__ == '__main__':
    window = Tk()
    window.title("Program de limbi")

    window.geometry("300x100")
    ef = EnglishFactory()
    sf = SpanishFactory()
    jf = JapanesseFactory()

    b1 = ef.createButton()
    b2 = sf.createButton()
    b3 = jf.createButton()

    b1.pack()
    b2.pack()
    b3.pack()

    window.mainloop()
