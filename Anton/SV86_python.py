import tkinter
from googletrans import Translator


class Button:
    def __init__(self, text, language):
        translator = Translator()
        translation = translator.translate(text, language)
        self.text = translation

    def draw(self):
        top = tkinter.Tk()
        b = tkinter.Button(top, text=self.text.text)
        b.pack()
        top.mainloop()


class ButtonFactoryFactory:
    @staticmethod
    def createButtonFactory():
        return ButtonFactory()


class ButtonFactory(ButtonFactoryFactory):
    @staticmethod
    def createButton(text, language):
        return Button(text, language)


if __name__ == "__main__":
    factoryFactory = ButtonFactoryFactory()
    buttonFactory = factoryFactory.createButtonFactory()
    text = input()
    limba = input()
    button = buttonFactory.createButton(text, limba)
    button.draw()
