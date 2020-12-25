'''
'''
from kivy.app import App
from kivy.lang import Builder


KV = '''
Label:
    text: 'pretty!'
'''

class Application(App):
    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    Application().run()
