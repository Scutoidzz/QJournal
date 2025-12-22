from PyQt6.QtWidgets import QApplication, QSplashScreen
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, QTimer
import sys
import os

def splash():
    # Check if QApplication already exists
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    
    # Use absolute path to the image
    image_path = "assets/journalsplash.png"
    print(f"Attempting to load splash image from: {image_path}")
    
    if not os.path.exists(image_path):
        print(f"ERROR: Image file not found at {image_path}")
        return app
        
    pixmap = QPixmap(image_path)
    if pixmap.isNull():
        print("ERROR: Failed to load image (invalid or corrupted)")
        return app
        
    print(f"Image loaded successfully: {pixmap.width()}x{pixmap.height()}")
    
    # Create splash screen
    splash_screen = QSplashScreen(pixmap, Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
    splash_screen.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
    splash_screen.setWindowIcon(QIcon("assets/qappicon.png"))

    # Show the splash screen
    splash_screen.show()
    print("Splash screen shown")
    
    # Process events to make sure the window is shown
    app.processEvents()
    
    # Simple wait using a loop with processEvents
    import time
    start_time = time.time()
    while time.time() - start_time < 5.0:  # 5 seconds
        app.processEvents()
        time.sleep(0.01)  # Small sleep to prevent 100% CPU usage
    
    splash_screen.close()
    print("Splash screen closed")
    
    # Return the app instance for further use
    return app

if __name__ == "__main__":
    splash()