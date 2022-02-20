import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.config import Config

from GUI import root


guiRoot = Builder.load_string(root.root)

def initAll():
    '''
    set attrs to specific widget, since using __init__ the pos set in kivy is omitted
    '''

    
    TimeInput = guiRoot.children[1].children[3]
    PlayButton = guiRoot.children[1].children[2]
    ReloadButton = guiRoot.children[1].children[1] 
    UserInput = TimeInput.children[1]
    Display = guiRoot.children[0]

    UserInput.time = ['-', '-', '-', '-']
    TimeInput.time = UserInput.time
    Display.time = UserInput.time
    PlayButton.time = UserInput.time

    Display.cicles = 0
    Display.getTimeInt = TimeInput.getTimeInt

    PlayButton.playTimer = Display.playTimer
    PlayButton.pauseTimer = Display.pauseTimer

    ReloadButton.reloadTimer = Display.reloadTimer
    
    SecArrow = TimeInput.children[0]
    MinArrow = TimeInput.children[2]
    SecArrow.children[0].id = 'secDw'
    SecArrow.children[1].id = 'secUp'
    MinArrow.children[0].id = 'minDw'
    MinArrow.children[1].id = 'minUp'

initAll()

class Temporizer3000App(App):

    def build(self):
        self.title = 'Temporizer 3000'
        return guiRoot

    def on_stop(self):
        width, height = guiRoot.parent.size
        Config.set('graphics', 'width', width)
        Config.set('graphics', 'height', height)
        Config.write()

    


Temporizer3000App().run()
