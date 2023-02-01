import win32gui
from pywinauto.application import Application
import time

windowtitle = "EmotivPRO 3.4.2.444"
target_window = win32gui.FindWindow(None, windowtitle)
print(target_window)
app =Application()
app.connect(handle=target_window)


while 1:
    print("send key q")
    app.window(title=windowtitle).send_keystrokes("q")
    time.sleep(1)
    print("send char q")

    app.window(title=windowtitle).send_chars("q")
