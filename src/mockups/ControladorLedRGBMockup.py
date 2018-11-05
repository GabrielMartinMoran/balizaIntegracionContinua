from tkinter import *

class ControladorLedRGB:

    def __init__(self, configuracion_led_rgb):
        self.__root = Tk()
        self.__root.title("Led")
        self.__root.update()

    def set_rgb(self, rgb):
        color = '#%02x%02x%02x' % rgb
        self.__root.configure(background=color)
        self.__root.update()