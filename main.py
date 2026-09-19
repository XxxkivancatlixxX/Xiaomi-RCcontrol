from evdev import InputDevice, ecodes, UInput
import select

kumanda_key = InputDevice("/dev/input/event18")
kumanda_cons = InputDevice("/dev/input/event19")

aparat = [kumanda_key, kumanda_cons]

ui = UInput({ecodes.EV_KEY: [ecodes.KEY_ENTER]})
ui1 = UInput({ecodes.EV_KEY: [ecodes.KEY_TAB]})

while True:
    ready, _, _ = select.select(aparat, [], [])

    for device in ready:
        for event in device.read():

            if event.type == ecodes.EV_KEY:

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
                    ui.write(ecodes.EV_KEY, ecodes.KEY_ENTER, event.value)
                    ui.syn()
                elif event.code == ecodes.KEY_APPSELECT:
                    print("appselect")

                elif event.code == ecodes.KEY_BACK:
                    print("back")

                elif event.code == ecodes.KEY_HOMEPAGE:
                    print("home")

                elif event.code == ecodes.KEY_VOLUMEDOWN:
                    print("volDOWN")

                elif event.code == ecodes.KEY_VOLUMEUP:
                    print("volUP")

                elif event.code == ecodes.KEY_VIDEO:
                    print("netflix")

                elif event.code == ecodes.KEY_YELLOW:
                    print("prime")

                elif event.code == ecodes.KEY_VOICECOMMAND:
                    print("voice")
                    ui1.write(ecodes.EV_KEY, ecodes.KEY_TAB, event.value)
