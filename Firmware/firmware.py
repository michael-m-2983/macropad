import board

from kmk.kmk_keyboard import KMKKeyboard
from kik.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11
]

keyboard.matrix = KeysScanner(
    pins=PINS, 
    value_when_pressed=False
)

keyboard.keymap = [
        [
            KC.A, 
            KC.DELETE, 
            KC.MACRO("Hello world!"), 
            KC.Macro(
                Press(KC.LCMD), 
                Tap(KC.S), 
                Release(KC.LCMD)
            ),
        ]
]

if __name__ == '__main__':
    keyboard.go()