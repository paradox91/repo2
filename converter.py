from font import Font, FontLoader
from textdrawer import TextDrawer

def getText():
    return 'Git'

class Font:
    pass

class FontLoader:
    def loadFont(self, directory):
        pass

class TextDrawer:
    def setFont(self, font):
        pass

    def draw(self, text):
        pass


text = getText()
font = FontLoader().loadFont('fancyFont/')
drawer = TextDrawer()
drawer.setFont(f)
drawer.draw(t)
