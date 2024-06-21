"""
https://uproger.com/pattern-abstraktnaya-fabrika-realizacziya-na-python/?ysclid=lxn0w59sdn601010634    
"""

"""
Абстрактная фабрика — это порождающий паттерн проектирования, который позволяет создавать семейства связанных объектов, 
не привязываясь к конкретным классам создаваемых объектов.
"""

class WindowFactory:
    @classmethod
    def create_window(cls, name):
        """Метод создания окна, возврашает класс окно"""
        return cls.Window(name)
    @classmethod
    def create_button(cls, name):
        """Метод создания кнопки, возврашает класс кнопки"""
        return cls.Button(name)
    


class MacOsFactory(WindowFactory):
    class Window:
        def __init__(self, name):
            self.name = name
            self.button = []
            self.style = 'Mac Os window style'
        def add_button(self, btn):
            self.button.append(btn.name)
        def show(self):
            print( '{} - {} and {}'.format(self.name, self.style, self.button))
    class Button:
        def __init__(self, name):
            self.name = name
            self.style = 'Mac Os button style'
            

class LinuxFactory(WindowFactory):
    class Window:
        def __init__(self, name):
            self.name = name
            self.button = []
            self.style = 'Ubuntu window style'
        def add_button(self, btn):
            self.button.append(btn.name)
        def show(self):
            print( '{} - {} and {}'.format(self.name, self.style, self.button))
    class Button:
        def __init__(self, name):
            self.name = name
            self.style = 'Ubuntu button style'
            

def create_dialog(factory):
    wind = factory.create_window('Form1')
    button = factory.create_button('Button1')
    wind.add_button(button)
    return wind


if __name__ == "__main__":
    # Допустим мы запустились на Linux
    w1 = create_dialog(LinuxFactory)
    w1.show()
    
    # или на MacOs
    w2 = create_dialog(MacOsFactory)
    w2.show()

    