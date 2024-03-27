from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.switch import Switch
from kivy.uix.progressbar import ProgressBar
from kivy.uix.spinner import Spinner


class FirstScreen(Screen):
    def __init__(self, name = "first"): #метод для створення об'єкта
        #у даній програмі використовуємо цей метод для створення початкового екрану
        #коли створюється об'єкт або викликається клас (-instantiation) то init автоматично запускається
        super().__init__(name = name)
        # викликає __init__ метод батьківського класу Screen, передаючи параметр name в якості аргументу
        # батьківський клас імпортований з бібліотеки kivy 
        layout = BoxLayout()
        
        btn1 = Button(text = "Go to SECOND SCREEN!") #змінна, віджет, властивість
        btn1.on_press = self.go_to_second #подія, яка викликає функцію
        layout.add_widget(btn1) #метод
        
        btn2 = Button(text = "Go to THIRD SCREEN!")
        btn2.on_press = self.go_to_third
        layout.add_widget(btn2)
        
        btn3 = Button(text = "Go to FOURTH SCREEN!")
        btn3.on_press = self.go_to_fourth
        layout.add_widget(btn3)
        
        btn4 = Button(text = "Go to FIFTH SCREEN!")
        btn4.on_press = self.go_to_fifth
        layout.add_widget(btn4)

        self.add_widget(layout) #додаємо layout до екземпляру
          
    def go_to_second(self):
        self.manager.transition.direction = "up" 
        # використовуємо атрибут self.manager для доступу до менеджера екранів 
        self.manager.current = "second"  
          
    def go_to_third(self):
        self.manager.transition.direction = "up"
        self.manager.current = "third"  

    def go_to_fourth(self):
        self.manager.transition.direction = "up"
        self.manager.current = "fourth"
     
    def go_to_fifth(self):
        self.manager.transition.direction = "up"
        self.manager.current = "fifth"


class SecondScreen(Screen):
    def __init__(self, name = "second"):
        super().__init__(name = name)
        # у second screen використовуємо self, тому що на відміну 
        # від first screen нам потрібно використовувати layout в інших методах, окрім init
        # без self створюється локальна змінна, яку не можна буде використовувати в інших методах

        self.layout = FloatLayout()

        self.btn = Button(text="Return to FIRST SCREEN!", size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.9})
        # size_hint=(0.5, 0.1) - атрибут встановлює відносний розмір кнопки щодо розміру батьківського віджета.
        # pos_hint={'center_x': 0.5, 'center_y': 0.9} - атрибут встановлює позицію кнопки відносно батьківського віджета
        self.btn.on_press = self.go_to_first
        self.layout.add_widget(self.btn)

        self.toggle_btn = ToggleButton(text="Toggle Button", size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        self.toggle_btn.bind(state=self.toggle_button_pressed) 
        # bind зв'язує подію і функцію
        self.layout.add_widget(self.toggle_btn)

        self.image = Image(source=r'C:\Users\Софія\Pictures\monkey.png', size_hint=(0.8, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.3})
        self.layout.add_widget(self.image)

        self.add_widget(self.layout)

    def go_to_first(self):
        self.manager.transition.direction = "down"
        self.manager.current = "first" 

    def toggle_button_pressed(self, instance, state):
    # передаємо посилання на кнопку і новий стан
    # instance не світиться, бо ми не використовуємо у функції,
    # але це потрібно, щоб функція знала з чим працювати
    # інакше - self - екземпляр цілого класу SecondScreen, а не саме кнопки
        if state == 'down':
            self.btn.opacity = 0  #атрибут
        else:
            self.btn.opacity = 1

class ThirdScreen(Screen):
    def __init__(self, name = "third"):
        super().__init__(name = name)
        
        layout = StackLayout(orientation='tb-lr', padding=[20], size_hint=(None, None), size=(400, 400),
                                   pos_hint={'center_x': 0.5, 'center_y': 0.5})
        #padding=[20] - атрибут встановлює відступи від країв StackLayout
        #size_hint=(None, None)-атрибут вказує на те, що розмір StackLayout не залежить від розміру батьківського віджета.
        #size=(400, 400)- атрибут встановлює фіксований розмір StackLayout. У вашому випадку встановлено розмір 400 на 400 пікселів.

        label = Label(text='Rate the monkey`s look:', size_hint=(1, None), height=100, font_size=30)
        layout.add_widget(label)
        # size_hint=(1, None) і height=100 -ширина пропорційна батьківському, але висота фіксована

        slider = Slider(min=0, max=100, value=50, size_hint=(1, None), height=100)
        layout.add_widget(slider)
        
        btn = Button(text = "Return to FIRST SCREEN!", size_hint=(1, None), height=100, font_size=30)
        btn.on_press = self.go_to_first
        layout.add_widget(btn)
# спершу додавала кнопку без layout в попередньому рядку через self (як у second screen). 
# Тому вона залишалась внизу і не відцентровувалась, бо не входила до layout
        self.add_widget(layout)
        
    def go_to_first(self):
        self.manager.transition.direction = "down"
        self.manager.current = "first"


class FourthScreen(Screen):
    def __init__(self, name = "fourth"):
        super().__init__(name = name)
        layout = GridLayout(cols=1)

        btn = Button(text = "Return to FIRST SCREEN!")
        btn.on_press = self.go_to_first
        layout.add_widget(btn)
        
        input = TextInput(text="Monkey`s name")
        layout.add_widget(input)

        switch = Switch(active=True)
        layout.add_widget(switch)

        self.add_widget(layout)

    def go_to_first(self):
        self.manager.transition.direction = "down"
        self.manager.current = "first"
        

class FifthScreen(Screen):
    def __init__(self, name = "fifth"):
        super().__init__(name = name)
        layout = FloatLayout()

        spinner = Spinner(text='Spinner', values=('Option 1', 'Option 2', 'Option 3'),
                          size_hint=(None, None), size=(400, 150), pos=(100, 700)) #відступ зліва і справа
        layout.add_widget(spinner)

        btn = Button(text = "Return to FIRST SCREEN!",size_hint=(None, None), size=(400, 150), pos=(400, 400))
        btn.on_press = self.go_to_first
        layout.add_widget(btn)

        bar = ProgressBar(value=50, max=100, size_hint=(None, None), size=(400, 150), pos=(700, 100))
        layout.add_widget(bar)
        
        self.add_widget(layout)
        
    def go_to_first(self):
        self.manager.transition.direction = "down"
        self.manager.current = "first"
                

class MyApp(App):
    def build(self): #метод
        sm = ScreenManager() #екземпляр кореневого віджета
        # ScreenManager - кореневий віджет, оскільки  відповідає за керування екранами 
        # у внутрішній структурі даних ScreenManager зберігаються усі екрани
        # відображення першого екрана стається через те, 
        # що за замовчуванням ScreenManager автоматично встановлює перший доданий екран як поточний
        sm.add_widget(FirstScreen()) 
        sm.add_widget(SecondScreen())
        sm.add_widget(ThirdScreen())
        sm.add_widget(FourthScreen())
        sm.add_widget(FifthScreen())
        return sm

MyApp().run()
