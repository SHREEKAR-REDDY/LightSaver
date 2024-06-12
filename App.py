import tkinter as tk
from LightSaver import set_max_brightness, set_min_brightness, increase_brightness

def create_gui():
    # Create a new window
    window = tk.Tk()

    # Set the window title
    window.title("DarkVader")

    # Create a button
    BTN_set_max_brightness = tk.Button(window, text="Max Bright", command=set_max_brightness)
    BTN_set_min_brightness = tk.Button(window, text="Min Bright", command=set_min_brightness)
    BTN_set_avg_brightness = tk.Button(window, text="Bright", command=increase_brightness)
    BTN_black_screen = tk.Button(window, text="Black Screen", command=create_black_screen)


    # Add the button to the window
    BTN_set_max_brightness.pack()
    BTN_set_min_brightness.pack()
    BTN_set_avg_brightness.pack()
    BTN_black_screen.pack()

    # Start the event loop
    window.mainloop()


def create_black_screen():
    black_screen = tk.Toplevel()
    black_screen.attributes('-fullscreen', True)
    black_screen.configure(background='black', cursor='none')
    set_min_brightness()

    def close_black_screen(event):
        black_screen.destroy()
        set_max_brightness()

    black_screen.bind('<Escape>', close_black_screen)
    black_screen.focus_set()

# Call the function to create the GUI
create_gui()
