from kivy.lang.builder import Builder
from kivy.uix.button import Button

playButton = '''
<PlayButton>
    font_size: '30dp'
    text: '1'
    font_name: 'Resources/GuifxV2Transports-YMJo.ttf'
'''

class PlayButton(Button):

    def on_release(self):
        self.parent.children[3].fixTime()
        if all([x == '0' or x == '-' for x in self.time]):
            return
        if self.text == '1':
            self.text = '2'
            self.playTimer()
        else:
            self.text = '1'
            self.pauseTimer()

        
        

Builder.load_string(playButton)

