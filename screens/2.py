from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager


class FirstScreen(Screen):
    def __init__(self, name="first"):
        super().__init__(name=name)

        layout = BoxLayout(orientation='vertical')

        btn1 = Button(text="Go to SECOND SCREEN!")
        btn1.bind(on_press=self.go_to_second)
        layout.add_widget(btn1)

        btn2 = Button(text="Go to THIRD SCREEN!")
        btn2.bind(on_press=self.go_to_third)
        layout.add_widget(btn2)

        btn3 = Button(text="Go to FOURTH SCREEN!")
        btn3.bind(on_press=self.go_to_fourth)
        layout.add_widget(btn3)

        btn4 = Button(text="Go to FIFTH SCREEN!")
        btn4.bind(on_press=self.go_to_fifth)
        layout.add_widget(btn4)

        self.add_widget(layout)

    def go_to_second(self, instance):
        self.manager.transition.direction = "up"
        self.manager.current = "second"

    def go_to_third(self, instance):
        self.manager.transition.direction = "up"
        self.manager.current = "third"

    def go_to_fourth(self, instance):
        self.manager.transition.direction = "up"
        self.manager.current = "fourth"

    def go_to_fifth(self, instance):
        self.manager.transition.direction = "up"
        self.manager.current = "fifth"


class SecondScreen(Screen):
    def __init__(self, name="second"):
        super().__init__(name=name)
        btn = Button(text="Return to FIRST SCREEN!")
        btn.bind(on_press=self.go_to_first)
        self.add_widget(btn)

    def go_to_first(self, instance):
        self.manager.transition.direction = "down"
        self.manager.current = "first"


class ThirdScreen(Screen):
    def __init__(self, name="third"):
        super().__init__(name=name)
        btn = Button(text="Return to FIRST SCREEN!")
        btn.bind(on_press=self.go_to_first)
        self.add_widget(btn)

    def go_to_first(self, instance):
        self.manager.transition.direction = "down"
        self.manager.current = "first"


class FourthScreen(Screen):
    def __init__(self, name="fourth"):
        super().__init__(name=name)
        btn = Button(text="Return to FIRST SCREEN!")
        btn.bind(on_press=self.go_to_first)
        self.add_widget(btn)

    def go_to_first(self, instance):
        self.manager.transit