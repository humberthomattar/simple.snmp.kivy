# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.popup import Popup
from get import SimpleSnmp
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.image import Image
from kivymd import snackbar as Snackbar
from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch
from kivymd.material_resources import DEVICE_TYPE
from kivymd.navigationdrawer import NavigationDrawer
from kivymd.selectioncontrols import MDCheckbox
from kivymd.theming import ThemeManager
from kivymd.time_picker import MDTimePicker


class KitchenSinkNavDrawer(NavigationDrawer):
    pass

class SnmpToolApp(App):
    h = 'Consultar'
    theme_cls = ThemeManager()
    nav_drawer = ObjectProperty()

    def build(self):
        Window.size = (450, 550)
        self.load_kv('main.kv')
        self.nav_drawer = KitchenSinkNavDrawer()

    def set_result_form(self, resultado):
        self.root.ids.textinput_resultado.text = resultado
        print resultado

    def get_values_form(self, ip, community):
        a = SimpleSnmp(ip, community)
        result = a.GetSNMP()
        result = result + '\n\nDados processados: '
        result = result + '\n- IP ' + ip
        result = result + '\n- Community ' + community
        self.set_result_form(result)

    def show_example_snackbar(self, snack_type):
        if snack_type == 'simple':
            Snackbar.make("Processando a requisicao. Aguarde!")
#        elif snack_type == 'button':
#            Snackbar.make("This is a snackbar", button_text="with a button!",
#                          button_callback=lambda *args: 2)
#        elif snack_type == 'verylong':
#            Snackbar.make("This is a very very very very very very very long "
#                          "snackbar!",
#                          button_text="Hello world")

if __name__ == "__main__":
    SnmpToolApp().run()
