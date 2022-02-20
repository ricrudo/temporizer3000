from kivy.lang.builder import Builder
from kivy.uix.button import Button

reloadButton = '''
<ReloadButton>
    font_size: '30dp'
    text: '9'
    font_name: 'Resources/GuifxV2Transports-YMJo.ttf'
'''

class ReloadButton(Button):
   
    def on_release(self):
        self.reloadTimer()
        self.parent.children[2].text = '1'
        


Builder.load_string(reloadButton)

