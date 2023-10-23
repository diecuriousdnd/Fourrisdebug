from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
# from kmk.modules.mouse_keys import MouseKeys
# from kmk.modules.modtap import ModTap
from kmk.hid import HIDModes
from kmk.scanners import DiodeOrientation
import board
keyboard = KMKKeyboard()
# modtap = ModTap()
layers_ext = Layers()
keyboard.modules.append(layers_ext)
# keyboard.modules.append(MouseKeys())
# keyboard.modules.append(modtap)

col_pins = (board.D8, board.D6, board.D4, board.D2, board.D12, board.D13, board.D15, board.D16)
row_pins = (board.D29, board.D27, board.D22, board.D23)
diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [ [
KC.B,                 KC.Y,      KC.O,       KC.U,                            KC.L,  KC.D,      KC.W,        KC.V,
KC.C,                 KC.I,      KC.E,       KC.A,                            KC.H,  KC.T,      KC.S,        KC.N,
KC.HT(KC.G, KC.LSFT), KC.X,      KC.J,       KC.K,                            KC.R,  KC.M,   KC.F,    KC.HT(KC.P, KC.RSFT), 
   KC.NO,  KC.HT(KC.MB_RMB, KC.Z),  KC.MB_LMB,  KC.HT(KC.TAB, KC.MO(1)),               KC.HT(KC.SPACE, KC.MO(2)), KC.ENTER,  KC.HT(KC.QUOTE, KC.Q), KC.NO],

[KC.ESC,             KC.HOME,    KC.UP,    KC.MW_UP,                         KC.N7,  KC.N8,  KC.N9,  KC.BSPC,  
KC.NO,               KC.LEFT,  KC.DOWN,     KC.RIGHT,                       KC.N4,  KC.N5,  KC.N6,  KC.MINUS, 
KC.LSFT,           KC.END,    KC.MB_MMB,   KC.MW_DN,                        KC.N1,  KC.N2,  KC.N3,  KC.PPLS, 
                     KC.NO,  KC.NO,  KC.NO,  KC.MO(1),                               KC.SPACE,  KC.N0,  KC.DOT, KC.NO],

[KC.ESC,     KC.LCTRL(KC.LSFT(KC.TAB)), KC.MS_UP, KC.LCTRL(KC.TAB),         KC.LCTRL(KC.F4),  KC.VOLU,    KC.VOLD,     KC.BSPC, 
KC.LCTRL(KC.A),  KC.MS_LT,            KC.MS_DN,    KC.MS_RT,                KC.LCTRL(KC.P),   KC.NO,      KC.COLON,    KC.MINUS, 
KC.LCTRL(KC.X),  KC.LCTRL(KC.C),     KC.LCTRL(KC.V), KC.LCTRL(KC.F),        KC.EXLM,          KC.COMM,    KC.DOT,      KC.QUESTION,
                        KC.NO, KC.MB_RMB, KC.MB_LMB, KC.NO,                         KC.MO(2), KC.LCTRL, KC.NO, KC.NO], 

] 
# keymap
if __name__ == '__main__': 
    keyboard.go(hid_type=HIDModes.USB)