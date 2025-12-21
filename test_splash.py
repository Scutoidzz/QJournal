from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap
import sys
import os

def test_window():
    app = QApplication(sys.argv)
    
    # Create main window
    window = QWidget()
    window.setWindowTitle("Test Window")
    layout = QVBoxLayout()
    
    # Try to load and display the image
    image_path = "/home/scutoid/Documents/QJournal/assets/journalsplash.png"
    status_label = QLabel(f"Trying to load: {image_path}")
    layout.addWidget(status_label)
    
    if os.path.exists(image_path):
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            image_label = QLabel()
            image_label.setPixmap(pixmap)
            layout.addWidget(image_label)
            status_label.setText("Image loaded successfully!")
        else:
            status_label.setText("ERROR: Failed to load image (invalid or corrupted)")
    else:
        status_label.setText(f"ERROR: File not found at {image_path}")
    
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    test_window()
