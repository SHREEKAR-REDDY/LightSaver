from pynput import keyboard
from screen_brightness_control import set_brightness

# 1. Figure out a way to detect non character keys ✔️
# 2. Write logic to kill the program when ctrl+c is pressed ✔️
# 3. Write logic to ignore all other key presses except 'ctrl, f5, f6, c' (Not needed)

# add a global variable to store the key combination
def on_press(key):
    if str(key) == "<78>":
        print("🌃  Dark mode activated.")
        # current_brightness = get_brightness(display=0)
        set_brightness(1)
    elif str(key) == "<77>":
        print("💡  Power levels at 400%")
        # current_brightness = get_brightness(display=0)
        set_brightness(50)
    elif str(key) == "<67>":
        exit()

def set_max_brightness():
    set_brightness(100)

def set_min_brightness():
    set_brightness(1)

def increase_brightness():
    set_brightness(60)

if __name__ == "__main__":
    print("🌞 Welcome to the brightness control program. It is a revolutionary program to control brightness (shocker!) 😲 ")
    print('⬆️  CTRL+ALT+N to increase') 
    print('⬇️  CTRL+ALT+M to decrease brightness')
    print('❌  CTRL+ALT+C to close the program')
    # Collect events until released
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(
        on_press=on_press)
    listener.start()
