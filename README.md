# n-back-task-pygame

This is a pygame tool for N-back task

![Alt text](https://github.com/habom2310/n-back-task-pygame/blob/main/Capture.JPG)

## Step to run
- Python 3.7
- Install required libraries: `pip install -r requirements.txt`
- Run `main_app.py`

## Main Features:
- Play sounds of numbers in sequence (pre-defined in the `sound_sequences.py`) 

- Log events with timestamp (saved to `data` folder):
    - start: start of the task
    - number: number played
    - pressed: button presses

- Can work even when the pygame window is not focused.

- Can work with joystick button (Logitech Extreme 3D), need to install the Logitech Profiler and map joystick button to a keyboard button.


