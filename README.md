# Random Mouse Mover

This Python script simulates random mouse movements and clicks on your computer screen, with a specific focus on the taskbar region. The script helps prevent your computer from going into sleep mode or locking the screen during periods of inactivity, ensuring that it remains active and responsive.

## Requirements

- Python 3.x
- `pyautogui` library (automatically installed if not found)

## How to Use

1. Make sure you have Python 3.x installed on your system.

2. Run the script by executing the following command:

   ```bash
   python random_mouse_mover.py
   
The script will check if the required pyautogui library is installed and install it if necessary.

Sit back and let the script do the work. It will move the mouse cursor randomly around the taskbar region and click occasionally to keep your computer awake.

To stop the script, press Ctrl+C. It will exit gracefully.

## Customization
You can adjust the time interval between mouse movements by changing the interval variable in the script. This value is in seconds.
  
   ```bash
   interval = 0.5  # Adjust this value as needed

## Disclaimer
This script is intended for educational and convenience purposes. Please use it responsibly and in compliance with your system's usage policies.
