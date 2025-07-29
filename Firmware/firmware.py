import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [
    board.GP7,  # down
    board.GP8,  # right
    board.GP9,  # center
    board.GP10, # left
    board.GP11  # up
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False
)

keyboard.keymap = [
    [
        KC.DOWN, KC.RIGHT, KC.ENTER, KC.LEFT, KC.UP
    ]
]

if __name__ == '__main__':
    keyboard.go()
