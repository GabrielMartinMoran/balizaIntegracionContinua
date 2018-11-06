from tkinter import *
from threading import Thread
import time

class ControladorLedRGB:

    __color_fondo = "white"

    def __init__(self, configuracion_led_rgb):
        thread = Thread(target=self.__iniciar_como_thread)
        thread.daemon = True
        thread.start()

    def __iniciar_como_thread(self):
        self.__root = Tk()
        self.__root.title("Led")
        self.__root.update()
        while(True):
            self.__root.configure(background=self.__color_fondo)
            self.__root.update()
            time.sleep(0.01)

    def set_rgb(self, rgb):
        self.__color_fondo = '#%02x%02x%02x' % rgb