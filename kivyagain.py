# encoding: utf-8

__version__ = "0.3.1"

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button

from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label



class AudioButton(Button):
    """
    Botón para reproducir música. Tiene una propiedad que apunta al mp3 que queremos
    reproducir.
    """
    archivo = StringProperty()
    sound = None

    def on_archivo(self, instancia, archivo):
        """
        Manejador de cambio de propiedad archivo. Cuando se setea el nombre,
        por ejemplo desde un archivo KV, esta función se llama, cargando el archivo
        a través de la clase SoundLoader
        """
        print("Se setea %s a %s" % (archivo, instancia))
        instancia.sound = SoundLoader.load(archivo)

    def on_press(self, *args, **kwargs):
        playing = self.sound.get_pos()
        if playing:
            self.sound.stop()
            self.sound.seek(0)
        self.sound.play()


class MyLayout(FloatLayout):
    """
    Este widget no tiene ningun comoprtamiento, pero es necesario para
    referenciarlo desde el archivo .kv
    """
    pass

class SoundboardApp(App):
    def build(self):
        return MyLayout()
        Window.clearcolor = (0, 0, 0, 0)

if __name__ == '__main__':
    SoundboardApp().run()



