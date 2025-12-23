from PyQt6.QtWidgets import QApplication, QSplashScreen
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, QTimer
import sys
import os

def splash():
    """Display splash screen on application startup.
    
    TODO:
    - Add progress indicators for loading steps
    - Add version information display
    - Add loading status messages
    - Implement proper error handling for missing assets
    - Add configuration options for splash duration
    - Add fade in/fade out animations
    - Add click to skip functionality
    - Add loading of application resources in background
    """
    # Check if QApplication already exists
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    
    # TODO: Use proper configuration for image paths
    # TODO: Add fallback for missing images
    # TODO: Add image validation and error handling
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
    
    # TODO: Make splash duration configurable
    # TODO: Add dynamic loading based on application startup time
    # TODO: Add proper event loop handling
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