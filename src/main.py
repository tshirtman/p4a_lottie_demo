'''
'''
from kivy.app import App
from kivy.lang import Builder


KV = '''
Label:
    text: 'pretty! \\nAnimation by yosif (https://lottiefiles.com/yoz)\\nAvailable at https://lottiefiles.com/42369-weather-wind'
    text_size: self.width, None
    halign: 'center'
'''

class Application(App):
    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    Application().run()
