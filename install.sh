#!/bin/bash

# QJournal Installation Script
# This script installs QJournal to /opt/qjournal and creates a desktop entry

set -e

APP_NAME="QJournal"
INSTALL_DIR="/opt/qjournal"
DESKTOP_FILE="/usr/share/applications/qjournal.desktop"
BIN_LINK="/usr/local/bin/qjournal"

echo "========================================="
echo "  QJournal Installation Script"
echo "========================================="
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo "Please run as root (use sudo)"
    exit 1
fi

echo "Installing QJournal to $INSTALL_DIR..."

# Create installation directory
mkdir -p "$INSTALL_DIR"

# Copy the executable
cp dist/QJournal "$INSTALL_DIR/"
chmod +x "$INSTALL_DIR/QJournal"

# Copy assets if they exist
if [ -d "assets" ]; then
    cp -r assets "$INSTALL_DIR/"
fi

# Create desktop entry
echo "Creating desktop entry..."
cat > "$DESKTOP_FILE" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=QJournal
Comment=A Personal Privacy-Focused Journal
Exec=$INSTALL_DIR/QJournal
Icon=$INSTALL_DIR/assets/qappicon.png
Terminal=false
Categories=Office;Utility;
Keywords=journal;diary;notes;
EOF

# Create symlink for command-line access
ln -sf "$INSTALL_DIR/QJournal" "$BIN_LINK"

# Update desktop database
if command -v update-desktop-database &> /dev/null; then
    update-desktop-database /usr/share/applications
fi

echo ""
echo "========================================="
echo "  Installation Complete!"
echo "========================================="
echo ""
echo "You can now run QJournal by:"
echo "  1. Searching for 'QJournal' in your application menu"
echo "  2. Running 'qjournal' from the terminal"
echo "  3. Running '$INSTALL_DIR/QJournal' directly"
echo ""
echo "To uninstall, run: sudo rm -rf $INSTALL_DIR $DESKTOP_FILE $BIN_LINK"
echo ""
