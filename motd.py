import curses
import random
import time
import re
import npyscreen


MOTD = """
=================.,=====================.,=====================.,=====================.,=====================.
|||||||||||||||| || ||||||||||||||||||| || ||||||||||||||||||| || ||||||||||||||||||| || ||||||||||||||||||| |
----------------.||.-------------------.||.-------------------.||.-------------------.||.-------------------.|
LPME  O  MMMMMM |||| MMMMMM  O  MMMMMM |||| MMMMMM  O  MMMMMM |||| MMMMMM  O  MMMMMM |||| MMMMMM  O  MMMMMM ||
----------------.||.-------------------.||.-------------------.||.-------------------.||.-------------------.|
MMMM  O  MMMMMM |||| MMMMMM  O  MMMMMM |||| MMMMMM  O   WAYQ  |||| MMMMMM  O  MMMMMM ||||  9/11   O  MMMMMM ||
----------------.||.-------------------.||.-------------------.||.-------------------.||.-------------------.|
MMMM  O  MMMMMM |||| BUNKER  O  MMMMMM |||| MMMMMM  O  MMMMMM |||| MMMMMM  O  MMMMMM |||| MMMMMM  O  MMMMMM ||
----------------.||.-------------------.||.-------------------.||.-------------------.||.-------------------.|
MMMM  O  MMMMMM |||| MMMMMM  O   CHAN  |||| MMMMMM  O  MMMMMM |||| MMMMMM  O  MMMMMM |||| MMMMMM  O  CANADA ||
----------------.||.-------------------.||.-------------------.||.-------------------.||.-------------------.|
MMMM  O  MMMMMM |||| MMMMMM  O  MMMMMM |||| MMMMMM  O  MMMMMM |||| CRYPTO  O   LOSS  |||| MMMMMM  O  MMMMMM ||
----------------.||.-------------------.||.-------------------.||#####################||.-------------------.|
MMMM  O  MMMMMM |||| MMMMMM  O  MMMMMM ||||  ALEX   O  MMMMMM |||#  |      #   |  |  #||| MMMMMM  O  MMMMMM ||
----------------.||.-------------------.||.-------------------.||#  |      #   |  |  #||.-------------------.|
MMMM  O  MMMMMM |||| MMMMMM  O  MMMMMM |||| MMMMMM  O  MMMMMM |||#####################||| MMMMMM  O  MMMMMM ||
----------------.||.-------------------.||.-------------------.||#  |      #   |     #||.-------------------.|
MMMM  O   JEWS  |||| MMMMMM  O  MMMMMM |||| MMMMMM  O  MMMMMM |||# 	|  |   #   |  __ #||| MMMMMM  O  Q-LARP ||
----------------.||.-------------------.||.-------------------.||#####################||.-------------------.|
MMMM  O  MMMMMM |||| ECHOES  O  MMMMMM |||| MMMMMM  O  MMMMMM |||| MMMMMM  O  MMMMMM |||| MMMMMM  O  MMMMMM ||
----------------.||.-------------------.||.-------------------.||.-------------------.||.-------------------.|
MMMM  O  MMMMMM |||| MMMMMM  O  MMMMMM |||| MMMMMM  O  MMMMMM |||| MMMMMM  O   JBCS  |||| MMMMMM  O  MMMMMM ||
----------------'||`-------------------'||`-------------------'||`-------------------'||`-------------------'|
=============I===´`=====================´`=====================´`=====================´`=====================´
 h or :h for |                Alola!~ Welcome to Bunkerchan, have an easy day!
     help    |     Source code can be found here: https://github.com/BigSlice/cursedboard
~~~~~~~~~~~~~´ NEWS: Images enabled! Thank eqi. sftp nanashi@bbs.shiptoasting.com 10 MB limit
"""

line_state = 0
flir = 0

class MotdTextfield(npyscreen.Textfield):
    '''Special textfield for animating the motd'''
    def __init__(self, *args, **keywords):
        super(MotdTextfield, self).__init__(*args, **keywords)
        self.syntax_highlighting = True
        random.seed(time.time())

    def update_highlighting(self, start=None, end=None, clear=False):
        global line_state
        global flir
        value = self.display_value(self.value)
        # highlighting color
        normal = self.parent.theme_manager.findPair(self, 'DEFAULT')
        yellow = self.parent.theme_manager.findPair(self, 'WARNING')
        cyan = self.parent.theme_manager.findPair(self, 'STANDOUT')
        green = self.parent.theme_manager.findPair(self, 'SAFE')
        blue = self.parent.theme_manager.findPair(self, 'NO_EDIT')
        red = self.parent.theme_manager.findPair(self, 'DANGER')

        color = [normal]*len(value)

        if line_state < 14:
            if value.find("~~~~~~~~~~~~~´") > -1:
                color[line_state] = blue
                line_state = (line_state + 1) % 18
        elif line_state == 14:
            if value.find("|     S") > -1:
                color[13] = blue
                line_state = (line_state + 1) % 18

        regex = re.compile("NEWS:")
        for group in regex.finditer(value):
            position = group.span()
            for i in range(position[0], position[1]):
                color[i] = random.choice([yellow, cyan, green, red])

        regex = re.compile("h or :h for")
        for group in regex.finditer(value):
            position = group.span()
            for i in range(position[0], position[1]):
                color[i] = red | curses.A_BOLD

        regex = re.compile("help")
        for group in regex.finditer(value):
            position = group.span()
            for i in range(position[0], position[1]):
                color[i] = red | curses.A_BOLD

        regex = re.compile("Alola!~")
        for group in regex.finditer(value):
            position = group.span()
            for i in range(position[0], position[1]):
                color[i] = yellow | curses.A_BOLD
				
        regex = re.compile("BUNKER")
        for group in regex.finditer(value):
            position = group.span()
            for i in range(position[0], position[1]):
                color[i] = cyan | curses.A_BOLD
				
        regex = re.compile("CHAN")
        for group in regex.finditer(value):
            position = group.span()
            for i in range(position[0], position[1]):
                color[i] = cyan | curses.A_BOLD
				
        regex = re.compile("help")
        for group in regex.finditer(value):
            position = group.span()
            for i in range(position[0], position[1]):
                color[i] = red | curses.A_BOLD
				
        regex = re.compile("CRYPTO")
        for group in regex.finditer(value):
            position = group.span()
            for i in range(position[0], position[1]):
                color[i] = red | curses.A_BOLD

        regex = re.compile("LOSS")
        for group in regex.finditer(value):
            position = group.span()
            for i in range(position[0], position[1]):
                color[i] = red | curses.A_BOLD
			
        regex = re.compile("ALEX")
        for group in regex.finditer(value):
            position = group.span()
            for i in range(position[0], position[1]):
                color[i] = red | curses.A_BOLD

        regex = re.compile("JEWS")
        for group in regex.finditer(value):
            position = group.span()
            for i in range(position[0], position[1]):
                color[i] = red | curses.A_BOLD
				
        regex = re.compile("9/11")
        for group in regex.finditer(value):
            position = group.span()
            for i in range(position[0], position[1]):
                color[i] = yellow | curses.A_BOLD
				
        regex = re.compile("WAYQ")
        for group in regex.finditer(value):
            position = group.span()
            for i in range(position[0], position[1]):
                color[i] = green | curses.A_BOLD
				
        regex = re.compile("ECHOES")
        for group in regex.finditer(value):
            position = group.span()
            for i in range(position[0], position[1]):
                color[i] = cyan | curses.A_BOLD
				
        regex = re.compile("CANADA")
        for group in regex.finditer(value):
            position = group.span()
            for i in range(position[0], position[1]):
                color[i] = red | curses.A_BOLD
				
        regex = re.compile("JBCS")
        for group in regex.finditer(value):
            position = group.span()
            for i in range(position[0], position[1]):
                color[i] = cyan | curses.A_BOLD
				
        regex = re.compile("MMMMMM")
        for group in regex.finditer(value):
            position = group.span()
            for i in range(position[0], position[1]):
                color[i] = random.choice([cyan, normal])
				
        regex = re.compile("#")
        for group in regex.finditer(value):
            position = group.span()
            for i in range(position[0], position[1]):
                color[i] = random.choice([red, yellow])
				
        regex = re.compile("MMMM")
        for group in regex.finditer(value):
            position = group.span()
            for i in range(position[0], position[1]):
                color[i] = random.choice([cyan, normal])

        regex = re.compile("O")
        for group in regex.finditer(value):
            position = group.span()
            for i in range(position[0], position[1]):
                if line_state == 17:
                    color[i] = blue
                    continue
                if random.random() > 0.97:
                    color[i] = red
                elif random.random() > 0.95:
                    color[i] = yellow
                else:
                    color[i] = green

        self._highlightingdata = color

class MotdPager(npyscreen.Pager):
    ''' Pager to display MOTD '''
    _contained_widgets = MotdTextfield
