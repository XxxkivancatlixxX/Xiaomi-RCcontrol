#Prerequisities#
```sh
sudo apt install python3-dev python3-pip libevdev-dev
python3 pip install evdev
```
###How to use?###

To use, just run the code via python 3 like this:

```sh
cd Xiaomi-RCcontrol/
python3 main.py
```
##Warning##
The device path is configured to my needs, so you would need to change it to your specific path, run the command below

```sh
python3 -c "import evdev; [print(f'Name: \"{evdev.InputDevice(p).name}\" | Path: {p}') for p in evdev.list_devices()]"
```
and then change the kumanda_key and kumanda_cons to the numbers you get (consumer control is kumanda_key and RC keyboard is kumanda_cons)



