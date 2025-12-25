from PyQt6.QtWidgets import QApplication, QSplashScreen
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, QTimer
import sys
import os
import logging
import random
import time


logging.basicConfig(filename="log.txt", level=logging.INFO)
def splash():
    # Check if QApplication already exists
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    
    image_path = "assets/journalsplash.png"
    print(f"Attempting to load splash image from: {image_path}")
    
    if not os.path.exists(image_path):
        logging.log(logging.ERROR, f"ERROR: Image file not found at {image_path}")
        return app

    if os.path.getsize(image_path) == 0:
        logging.log(logging.ERROR, f"ERROR: Image file is empty at {image_path}")
        return app

    if not os.path.isfile(image_path):
        logging.log(logging.ERROR, "Is not a file")
        return app
        
    pixmap = QPixmap(image_path)
    if pixmap.isNull():
        logging.log(logging.ERROR, "Failed to load image (invalid or corrupted)")
        return app
        
    logging.log(logging.INFO, f"Image loaded successfully: {pixmap.width()}x{pixmap.height()}")
    
    # Create splash screen
    splash_screen = QSplashScreen(pixmap, Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
    splash_screen.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
    splash_screen.setWindowIcon(QIcon("assets/qappicon.png"))

    # Show the splash screen
    splash_screen.show()
    logging.log(logging.INFO, "Splash screen shown")
    
    # Process events to make sure the window is shown
    app.processEvents()
    
    import time
    start_time = time.time()

    randomtime = random.randint(2, 5)

    while time.time() - start_time < randomtime:  # Light work no reaction
        app.processEvents()
        time.sleep(0.01)  # Small sleep to prevent 100% CPU usage
    
    splash_screen.close()
    logging.log(logging.INFO, "Splash screen closed")
    
    # Return the app instance for further use
    return app

if __name__ == "__main__":
    splash()