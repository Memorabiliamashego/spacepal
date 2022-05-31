# from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock



Window_size = (310, 580)


class MainApp(MDApp):


    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"

        global sm
        sm = ScreenManager()
        sm.add_widget(Builder.load_file("dashboard.kv"))
        sm.add_widget(Builder.load_file("preloader.kv"))
        sm.add_widget(Builder.load_file("login.kv"))
       
        # sm.add_widget(Builder.load_file("ui.kv"))
        

        return sm

    # def on_start(self):
    #     Clock.schedule_once(self.login, 5)

    # def login(self, *args):
    #     sm.current = "login"




MainApp().run()






#################################################################### FIRST SCREEN TRANSITION EX



# class Main(MDApp):
#     def build(self):
#         Builder.load_file("ui.kv")

#         sm = ScreenManager(transition = FadeTransition())
#         sm.add_widget(Demo1(name = 'demo1'))
#         sm.add_widget(Demo2(name = 'demo2'))
#         return sm

# Main().run()