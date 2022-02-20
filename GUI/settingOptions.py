from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout

from GUI import playButton, reloadButton, timeInput

settingOptions = '''
<SettingOptns>
    orientation: 'horizontal'
    Widget:
        size_hint: 1, 1
    TimeInput:
        size_hint: 4, 1
    PlayButton:
        size_hint: 2, 1
        
    ReloadButton:
        size_hint: 2, 1
    Widget:
        size_hint: 1, 1
    
'''

Builder.load_string(settingOptions)

class SettingOptns(BoxLayout):
    pass


