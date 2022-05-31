from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.clock import Clock


Window.size = (400, 600)
class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"



class LoginPage(MDApp):

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("preloader.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        return screen_manager

    

    def on_start(self):
        Clock.schedule_once(self.login, 5)

    def login(self, *args):
        screen_manager.current = "login"

    def back_button(self, *args):
        if screen_manager.current == "login":
            current_scr = screen_manager.add_widget(Builder.load_file("preloader.kv"))
        return current_scr


# Use this if you call a function from App class:

# on_press: app.doThis()
# And use this if you call a function from Screen class:

# on_press: root.doThis()



if __name__ == "__main__":
    LoginPage().run()

