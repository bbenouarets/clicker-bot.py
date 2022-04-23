import pyautogui

class Clicker:
    def __init__(self, app: str = None) -> None:
        # App is the name of the application to be clicked
        # If app is None, the default application will be clicked (e.g. Chrome)
        self.app = app
        if app is None:
            self.app = "chrome.exe"
        
    def click(self, x: int, y: int, pause: int = 10.0) -> None:
        # x and y are the coordinates of the mouse click
        pyautogui.click(x, y)
        pyautogui.PAUSE = pause
        
    def get(self) -> None:
        while True:
            # Get the current mouse position
            x, y = pyautogui.position()
            print(f"Current Mouse Position: X: {x} Y: {y}")
            pyautogui.PAUSE = 1.0
            
            
if __name__ == "__main__":
    clicker = Clicker()
    clicker.get()