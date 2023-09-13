import os
import platform
import random
import time

def run_mouse_movement_script():
    # Check if required packages are installed and install them if needed
    try:
        import pyautogui
    except ImportError:
        try:
            # Attempt to install pyautogui quietly
            if platform.system() == "Windows":
                os.system("pip install pyautogui --user > nul 2>&1")
            else:
                os.system("pip3 install pyautogui --user > /dev/null 2>&1")
            import pyautogui
        except ImportError:
            # If installation fails, exit gracefully
            print("Error: Required packages not found, and automatic installation failed.")
            return
    
    # Function to move the mouse cursor to a random position on the screen
    def move_mouse():
        screenWidth, screenHeight = pyautogui.size()  # Get the screen resolution
        x = random.randint(0, screenWidth)
        y = random.randint(int(screenHeight * 0.999), int(screenHeight))
        
        pyautogui.moveTo(x, y, duration=0.1)  # Move the mouse cursor to (x, y) in 0.1 second
        pyautogui.click()  # Click the mouse
    
    # Specify the time interval (in seconds) for moving the mouse
    interval = 0.5  # Adjust this value as needed
    
    try:
        while True:
            move_mouse()
            time.sleep(interval)
    except KeyboardInterrupt:
        pass  # Exit gracefully when the user presses Ctrl+C

# Call the function to execute the mouse movement script
if __name__ == "__main__":
    run_mouse_movement_script()
