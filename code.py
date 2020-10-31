# CircuitPython demo - I2C scan
#
# If you run this and it seems to hang, try manually unlocking
# your I2C bus from the REPL with
#  >>> import board
#  >>> board.I2C().unlock()

import time
import board
import keypad_i2c

i2c = board.I2C()
kp = keypad_i2c.keypad_i2c(i2c)

while True:
    try:
       key, dur = kp.key_pressed
    except:
       key = 0x00

    if key != 0x00:
        print(key,dur)
    time.sleep(.5)



while not i2c.try_lock():
    pass

try:
    print("I2C addresses found:", [hex(device_address)
        for device_address in i2c.scan()])
    while True:
        key, dur = kp.key_pressed()
        if key != 0x00:
            print(key)
            print('test')
        time.sleep(0.1)

finally:  # unlock the i2c bus when ctrl-c'ing out of the loop
    i2c.unlock()