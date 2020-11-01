"""
CircuitPython Demo Program November 2020

https://github.com/infrapale/PyPortal_VA_Control
HW:
    PyPortal
    I2C KeyPad

"""


import time
import board
import keypad_i2c

i2c = board.I2C()
kp = keypad_i2c.keypad_i2c(i2c)

menu_state = 'Alku'

def nop():
    pass

def mh1_paalle():
    print('mh1_paalle')

def mh1_pois():
    print('mh1_pois')

def piha_paalle():
    print('piha_paalle')

def piha_pois():
    print('piha_pois')

# row_buff = [' ',' ',' ']
row_list = [0,12,24]
btn_list = ['A','B','C']

menu_dict = {
   'Alku':
       { '01':['Alku','MH1 paalle', mh1_paalle],
         '02':['Alku','MH1 pois', mh1_pois],
         '11':['Ulko','Ulkovalot', nop]
        },
    'Ulko' :
        {'01':['Ulko','Piha paalle', piha_paalle],
         '02':['Ulko','Piha pois', piha_pois],
         '12':['Alku','Alkuun', nop]
        }
   }
print(menu_state)

def print_menu(state):
    sub_keys = list(menu_dict[state].keys())
    for skey in sub_keys:
        print(skey,menu_dict[state][skey][1])
    print(state + '>')

while True:
    try:
       key, dur = kp.key_pressed
    except:
       key = 0x00

    if key != 0x00:
        key_str = chr(key) + chr(dur)
        print(key_str)
        sub_keys = list(menu_dict[menu_state].keys())
        sub_keys.sort(reverse=False)
        if key_str in sub_keys:
            new_menu = menu_dict[menu_state][key_str][0]
            print(menu_dict[menu_state][key_str][1])
            menu_dict[menu_state][key_str][2]()
            menu_state = new_menu
        print_menu(menu_state)
    time.sleep(.5)