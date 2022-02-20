from kivy.uix.label import Label
from kivy.lang.builder import Builder
from kivy.clock import Clock 

display = '''
<DisplayLabel>
    canvas.before:
        Color:
            rgb: 0,0,0
        Rectangle:
            pos: self.pos
            size: self.size
    text: '00:00'
    font_name: 'Resources/digital-7.regular.ttf'
    font_size: '140dp'
    color: 1, 1, 1
'''

class DisplayLabel(Label):

    def playTimer(self):
        if not self.cicles:
            self.reloadTimer()
        self.clock = Clock.schedule_interval(self.updatedisplay, 1)

    def pauseTimer(self):
        self.clock.cancel()

    def reloadTimer(self):
        if hasattr(self, 'clock'):
            self.clock.cancel()
        self.actualTime = self.getTimeInt()
        self.cicles = (self.actualTime[0] * 60) + self.actualTime[1] 
        self.showTime()

    def showTime(self):
        if self.actualTime[1] < 0:
            self.actualTime[0] -= 1 
            self.actualTime[1] = 59
        timeText = [str(x) for x in self.actualTime]
        for i, x in enumerate(timeText):
            if len(x) == 1:
                timeText[i] = f'0{x}'
        timeText = ':'.join(timeText)
        self.text = timeText
        b = 1
        g = 1
        if self.cicles < 60:
            b =  self.cicles/60
        if self.cicles < 30:
            g = self.cicles/30
        self.color = 1, g, b
            

    def updatedisplay(self, *clock):
        self.cicles -= 1
        self.actualTime[1] -= 1
        self.showTime()
        if not self.cicles:
            self.clock.cancel()
            self.parent.children[1].children[2].text = '1'
            self.countAlert = 0
            self.clock_alert = Clock.schedule_interval(self.alert, 0.4)

    def alert(self, *clock):

        self.countAlert += 1

        if self.countAlert % 2 == 0:
            self.canvas.before.children[0].rgb = 0,0,0
        else:
            self.canvas.before.children[0].rgb = 0.5,0.5,0.5
        if self.countAlert == 12:
            self.clock_alert.cancel()


Builder.load_string(display)
