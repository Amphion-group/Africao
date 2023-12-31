from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label


class MyGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)
    last_name = ObjectProperty(None)
    pass
    # def __init__(self, **kwargs):
    #     super(MyGrid, self).__init__(**kwargs)
    #     self.cols = 1
    #     self.inside = GridLayout()
    #     self.inside.cols = 2
    #
    #     self.inside.add_widget(Label(text="name"))
    #     self.name = TextInput()
    #     self.inside.add_widget(self.name)
    #
    #     self.inside.add_widget(Label(text="last name"))
    #     self.last_name = TextInput()
    #     self.inside.add_widget(self.last_name)
    #
    #     self.inside.add_widget(Label(text="email"))
    #     self.email = TextInput()
    #     self.inside.add_widget(self.email)
    #
    #     self.add_widget(self.inside)
    #
    #     self.submit = Button(text="submit", size_hint=(None, None), size=(dp(100), dp(40)))
    #     self.submit.bind(on_press=self.login)
    #     self.add_widget(self.submit)
    #

    def login(self):
        name = self.name.text
        last_name = self.last_name.text
        email = self.email.text
        print(name, last_name, email)


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()
