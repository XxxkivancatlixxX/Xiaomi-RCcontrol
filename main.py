
from evdev import InputDevice, ecodes
import select

kumanda_key = InputDevice("/dev/input/event18")
kumanda_cons = InputDevice("/dev/input/event19")

aparat = [kumanda_key, kumanda_cons]

while True:
    ready, _, _ = select.select(aparat, [], [])

    for device in ready:
        for event in device.read():
            if event.code == ecodes.KEY_UP:
                print("UP")

            elif event.code == ecodes.KEY_DOWN:
                print("DOWN")

            elif event.code == ecodes.KEY_LEFT:
                print("LEFT")

            elif event.code == ecodes.KEY_RIGHT:
                print("RIGHT")

            elif event.code == ecodes.KEY_SELECT:
                print("OK")
