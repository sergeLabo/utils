
class VirtualGl:
    pass

class VirtualEvents:
    pass

try:
    from bge import logic as gl
except:
    gl = VirtualGl()

try:
    from bge import events
except:
    events = VirtualEvents()


NUMBER_PAD_KEYS = { events.PAD0: 0,
                    events.PAD1: 0,
                    events.PAD2: 0,
                    events.PAD3: 0,
                    events.PAD4: 0,
                    events.PAD5: 0,
                    events.PAD6: 0,
                    events.PAD7: 0,
                    events.PAD8: 0,
                    events.PAD9: 0,
                    events.PADPERIOD: 0,
                    events.PADSLASHKEY: 0,
                    events.PADASTERKEY: 0,
                    events.PADMINUS: 0,
                    events.PADENTER: 0,
                    events.PADPLUSKEY: 0}


class KeyFactory:

    def __init__(self, key):

        self.key = key
        self.state = 0

    def key_update(self):

        if gl.keyboard.events[self.key] == gl.KX_INPUT_JUST_ACTIVATED:
            NUMBER_PAD_KEYS[self.key] = 1
            self.state = 1


class Keyboard(dict):
    """Crée une usine pour chaque touche de NUMBER_PAD_KEYS dans un dict."""

    def __init__(self):

        for key, val in NUMBER_PAD_KEYS.items():

            self[key] = KeyFactory(key)

    def keyboard_update(self):
        """Pour actualiser à chaque frame"""

        for key, val in NUMBER_PAD_KEYS.items():
            self[key].update()


if __name__ == '__main__':
    kb = Keyboard()
