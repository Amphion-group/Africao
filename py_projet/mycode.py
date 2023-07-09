from kivy.app import App

from kivy.uix.label import Label

class myapp(App):
    def build(self):
        return Label(text = "bonjour")


if __name__ == '__main__':
    myapp().run()