from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

timeInput = '''
<TimeInput>:
    orientation: 'horizontal'
    Arrows:
        size_hint: 1, 1
    UserInput:
        font_size: '28dp'
        text: '00:00'
        size_hint: 3, 1
        multiline: False
        border: [0,0,0,0]
        padding: [4,2,0,0]
    Arrows:
        size_hint: 1, 1


<Arrows@BoxLayout>
    orientation: 'vertical'
    Button:
        font_name: 'Resources/GuifxV2Transports-YMJo.ttf'
        text: 'w'
        font_size: '20dp'
        on_release: root.parent.pressArrow(self)
    Button:
        font_name: 'Resources/GuifxV2Transports-YMJo.ttf'
        text: 's'
        font_size: '20dp'
        on_release: root.parent.pressArrow(self)

'''

class UserInput(TextInput):

    def insert_text(self, substring, from_undo=False):
        self.parent.parent.parent.children[0].cicles = 0
        s = substring[:]
        if substring in ('1234567890'):
            cur_pos = self.cursor[0]
            if '-' in self.time:
                if cur_pos == 5: self.time.append(s)
                elif cur_pos in [1, 2]: self.time.insert(cur_pos, s)
                elif cur_pos in [4]: self.time.insert(cur_pos-1, s)
                else: return
                self.time.pop(0)
                self.parent.putText(cur_pos)
            
    def do_backspace(self, from_undo=False, mode='bkspc'):
        self.parent.parent.parent.children[0].cicles = 0
        cur_pos = self.cursor[0]
        if cur_pos in [1,2]: self.time.pop(cur_pos - 1)
        elif cur_pos in [4,5]: self.time.pop(cur_pos - 2)
        else: return
        self.time.insert(0, '-')
        self.parent.putText(cur_pos)


class TimeInput(BoxLayout):

    def putText(self, cur_pos=5):
        flag = False
        for i, x in enumerate(self.time):
            if x != '-':
                flag = True
            if flag and x == '-':
                self.time[i] = '0'

        text = ''.join(self.time[:2]) + ':' + ''.join(self.time[2:])
        self.children[1].text = text.replace('-', '0')
        self.children[1].cursor = (cur_pos,1)

    def fixTime(self, time=None):
        if not time:
            time = self.getTimeInt()

        if time[1] > 59:
            time[0] += 1
            time[1] -= 60
        elif time[1] < 0:
            time[0] -= 1
            if time[0] >= 0: 
                time[1] += 60
            else:
                time = [0,0]

        if time[0] < 0:
            time[0] = 0
        elif time[1] > 99:
            time = [99, 59]

        time = [str(x) for x in time]
        for i, x in enumerate(time):
            if len(x) == 1:
                if x == '0':
                    x = '-'
                time[i] = f'-{x}'
        self.time[:2] = time[0][0], time[0][1]
        self.time[2:] = time[1][0], time[1][1]
        self.putText()

    def pressArrow(self, obj):
        time = self.getTimeInt()
        value = 'Up' in obj.id and 1 or -1
        if 'min' in obj.id: time[0] += value
        elif 'sec' in obj.id: time[1] += value
        self.fixTime(time=time)
        self.parent.parent.children[0].cicles = 0

    def getTimeInt(self):
        return [int(''.join(self.time[:2]).replace('-', '0')), int(''.join(self.time[2:]).replace('-', '0'))]



Builder.load_string(timeInput)

