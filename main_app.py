import pygame
import sys
import datetime
import time
from pygame_button import PygameButton
import utils
import glob 
import os
import win32gui
from pywinauto.application import Application
# from serial import Serial
# import socket_client

# port_names = ["COM1", "COM2", "COM3"]

# initialize pywinauto
windowtitle = "EmotivPRO 3.4.2.444"
target_window = win32gui.FindWindow(None, windowtitle)
print(f"{windowtitle}: {target_window}")
app =Application()
try:
    app.connect(handle=target_window)
    print("App connected")
except:
    print(f"Initialize fail! Open the {windowtitle} before open the nback")

# initialize pygame
soundfile_paths = glob.glob(os.path.join(os.path.dirname(__file__),'sound_samples/*.wav'))
print(soundfile_paths)
pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.init()
pygame.mixer.init()

# init variables
done = False
is_running = False
is_statusbar = False
n_task = 0
statusbar_counter = 0
sound_counter = 0
time_between_number = 2
clock_rate = 10
current_index = 0
number_sequence = []
is_btnSet1_selected = False
is_btnSet2_selected = False
increment_id = utils.get_latest_id() + 1
save_path=""
clock = pygame.time.Clock()

# logging variables settings
data = []

# Serial COM settings
# ser = Serial()
# ser.baudrate = 19200

# is_ser = True
# for port in port_names:
#     ser.port = port
#     try:
#         ser.open()
#         print("Port open: " + port)
#         break
#     except:
#         is_ser = False
#         print(f"Port {port} is not available")

# pynput settings
from pynput import keyboard
from pynput.keyboard import Key, Controller
keyboard_controller = Controller()

def on_press(key):
    global is_running
    global status_text
    global statusbar_counter
    global is_statusbar
    global data
    number_sequence

    try: k = key.char # single-char keys
    except: k = key.name # other keys
    if 'char' in dir(key):     
        if key.char == 'q':
            timestamp = round(time.time() * 1000)
            datapoint = {"event": "pressed", "time": timestamp}
            try: 
                screen.fill(green)
            except:
                pass
            print(datapoint)
            data.append(datapoint)
            log_data_once(datapoint, save_path)
            print("q pressed")
            app.window(title=windowtitle).send_keystrokes("q")
            # if is_ser:
            #     ser.write(b'1')
            # socket_client.send(str.encode(f'{str(increment_id).zfill(3)}-1'))

        if key.char == 's':
            if not is_running:
                start_nback()
                app.window(title=windowtitle).send_keystrokes("s")
            # if is_ser:
            #     ser.write(b'2')
            # socket_client.send(str.encode(f'{str(increment_id).zfill(3)}-2'))

        if key.char == 'x':
            # socket_client.send(str.encode(f'{str(increment_id).zfill(3)}-3'))
            stop_nback()
            app.window(title=windowtitle).send_keystrokes("x")
            # if is_ser:
            #     ser.write(b'3')

lis = keyboard.Listener(on_press=on_press)
lis.start() # start to listen on a separate thread
# lis.join() # no this if main thread is polling self.keys

# background
white = (255, 255, 255)
# text color
black = (0, 0, 0)
#green
green = (0, 255, 0)
# light shade of the button
color_light = (200,200,200)  
# dark shade of the button
color_dark = (140,140,140)

# -------- Set up the Window -----------
# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
width = SCREEN_WIDTH
height = SCREEN_HEIGHT

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("N-Back Task")

# program text settings
label_text_font = pygame.font.SysFont("Calibri", 50)
label_text = label_text_font.render('N-Back Task', True, black)
label_text_center = (int(width/2),int(height/5))

def display_number(number, screen):
    nback_text_font = pygame.font.SysFont("Calibri", 70)
    nback_text = nback_text_font.render(str(number), True, black)
    screen.blit(nback_text, screen.blit(nback_text, nback_text.get_rect(center = (width/2,height/2))))

# button text setting 
btnStart_text = "Start"
btnStart_textsize = 40
btnStart_textcolor = (0,0,0)
btnStart_size = (200,120)
btnStart_center = (int(width/2),int(3*height/4))
btnStart = PygameButton(btnStart_center, btnStart_size, color_light, color_dark, btnStart_text, btnStart_textsize, btnStart_textcolor)

# ------- Status bar settings -----------
def status_bar(text, screen):
    # status bar
    text_font = pygame.font.SysFont("Calibri", 20)
    text_screen = text_font.render(text, True, black)
    screen.blit(text_screen, (5,height-20))

# -------- Playing sound sequence -----------
def play_sound(number):
    filepath = soundfile_paths[number-1]
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()

# -------- Logging data to file -----------
def log_data_all(data):
    global increment_id
    # global save_path
    save_path = f"logs/{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{str(increment_id).zfill(3)}.csv"
    increment_id += 1
    with open(save_path, "w+") as f:
        f.write("time,event\n")
        for datapoint in data:
            f.write(str(datapoint["time"]) + "," + str(datapoint["event"]) + "\n")
    
    print("File saved to: " + save_path)
    return save_path

def log_data_once(data_point, save_path):
    # global save_path
    with open(save_path, "a") as f:
        f.write(str(data_point["time"]) + "," + str(data_point["event"]) + "\n")

    return save_path

# ---------- Start/Stop the nback ------
def start_nback():
    global is_running
    global status_text
    global statusbar_counter
    global is_statusbar
    global number_sequence
    global data
    global save_path
    global increment_id

    save_path = f"logs/{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{str(increment_id).zfill(3)}.csv"
    increment_id += 1
    with open(save_path, "w+") as f:
        f.write("time,event\n")

    is_running = True
    number_sequence = utils.get_sound_sequences()
    timestamp = round(time.time() * 1000)
    datapoint = {"event": "Start", "time": timestamp}
    print(datapoint)
    data.append(datapoint)
    log_data_once(datapoint, save_path)

def stop_nback():
    global is_running
    global data
    global status_text
    global statusbar_counter
    global is_statusbar
    global save_path
    global increment_id

    timestamp = round(time.time() * 1000)
    datapoint = {"event": "Stop", "time": timestamp}
    print(datapoint)
    data.append(datapoint)
    log_data_once(datapoint, save_path)

    is_running = False
    save_path = log_data_all(data)
    status_text = f"File save to {save_path}"
    statusbar_counter = clock_rate * 3
    is_statusbar = True

# -------- Main Program Loop -----------

while not done:
    screen.fill(white)

    # print(_joystick.get_button(0))

    # --- Sound playing -----
    
    if is_running:
        if sound_counter == 0:
            number = number_sequence[current_index]
            play_sound(number)
            timestamp = round(time.time() * 1000)
            sound_counter = clock_rate*time_between_number
            datapoint = {"event": number, "time": timestamp}
            print(datapoint)
            data.append(datapoint)
            log_data_once(datapoint, save_path)
        else:
            sound_counter -= 1

        if sound_counter == 0:
            if current_index == len(number_sequence)-1:
                is_running = False
                sound_counter = 0
                current_index = 0
                save_path = log_data_all(data)
                status_text = f"File saved to {save_path}"
                statusbar_counter = clock_rate * 3
                is_statusbar = True
                data = []
            else:
                current_index += 1


    # --- Event handler -----
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.

        #checks if a mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and is_running == False:
            #if the mouse is clicked on the
            mouse_pos = pygame.mouse.get_pos()
            # print(mouse_pos)

            # button the game is terminated
            if btnStart.check_click(mouse_pos):
                print("Start button is clicked")
                start_nback()
                    
    # ------------ Start drawing ---------------            

    if is_statusbar == True:
        status_bar(status_text, screen)
        statusbar_counter -= 1
        if statusbar_counter == 0:
            is_statusbar = False
            status_text = ""
    if is_running == False:
        btnStart_text = "Start"
        screen.blit(label_text, label_text.get_rect(center = label_text_center))
        btnStart.draw(screen)
    else:
        btnStart_text = "Stop"
        number = number_sequence[current_index]
        display_number(number, screen)
        btnStart.draw(screen)

    # updates the frames of the game
    pygame.display.update()

    clock.tick(clock_rate)

# if is_ser:
#     ser.close()
pygame.quit()