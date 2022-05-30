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
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("preloader.kv"))
        return screen_manager

    

class SplashScreen():
    """This class will show the splash screen of SpacePal"""
    pass

class HomeScreen():
    """This class will show the Home screen of SpacePal"""
    pass    

class WindowManager(ScreenManager):
    """This class will handle the screen transitions"""
    pass

    # def on_start(self):
    #     Clock.schedule_once(self.login, 5)

    # def login(self, *args):
    #     screen_manager.current = "login"



if __name__ == "__main__":
    LoginPage().run()

