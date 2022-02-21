from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

from GUI import playButton, reloadButton, timeInput

settingOptions = '''
<SettingOptns>
    orientation: 'horizontal'
    HiddenBtn:
        size_hint: 1, 1
        on_release: root.blackDisplay()
    TimeInput:
        size_hint: 4, 1
    PlayButton:
        size_hint: 2, 1
        
    ReloadButton:
        size_hint: 2, 1
    HiddenBtn:
        size_hint: 1, 1
        on_release: root.setPos()

<HiddenBtn@Button>
    background_down: ''
    background_normal: ''
    background_color: 0,0,0, 0

'''

Builder.load_string(settingOptions)

class SettingOptns(BoxLayout):

    def setPos(self):
        top = self.get_root_window().top
        left = self.get_root_window().left
        width, height = self.get_root_window().size
        Config.set('graphics', 'position', 'custom')
        Config.set('graphics', 'top', top)
        Config.set('graphics', 'left', left)
        Config.set('graphics', 'width', width)
        Config.set('graphics', 'height', height)
        Config.write()
        print(Config.filename)

    def blackDisplay(self):
        self.parent.children[0].color = 0,0,0


