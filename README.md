# The Light Saver
***

## Description

### LightSaver Usage Instructions

- Run the `LightSaver.exe` after creating the executable file
- Press `CTRL+ALT+n` to decrease the brightness to 1
- Press `CTRL+ALT+m` to increase the brightness to 50

> **NOTE:**  
> By default, the primary screen brightness is affected.

### Watchmen Usage Instructions

Need to keep your screen awake?

- Run the `Watchmen.exe` after creating the executable file
- You can go AFK (Away From Keyboard) and your PC will never fall asleep

***

## Installation for Windows
**Step 1:**
```powershell
pip install pyinstaller
```

**Step 2:**
```powershell
pyinstaller --onefile 'LightSaver.py'

pyinstaller --onefile 'Watchmen.py'

pyinstaller --onefile 'App.py'
```

**Step 3:**
- Find the `.exe` in `dist` folder

***

## Future Improvements

- Combine the `Watchmen` into `LightSaver`