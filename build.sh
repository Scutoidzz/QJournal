#!/bin/bash

# QJournal Build Script
# Builds a standalone executable using PyInstaller

set -e

echo "========================================="
echo "  Building QJournal"
echo "========================================="
echo ""

# Check if PyInstaller is installed
if ! command -v pyinstaller &> /dev/null; then
    echo "Error: PyInstaller is not installed"
    echo "Install it with: pip install pyinstaller"
    exit 1
fi

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf build/ dist/

# Build the application
echo "Building application..."
pyinstaller QJournal.spec --clean

# Check if build was successful
if [ -f "dist/QJournal" ]; then
    echo ""
    echo "========================================="
    echo "  Build Complete!"
    echo "========================================="
    echo ""
    echo "Executable location: dist/QJournal"
    echo "Size: $(du -h dist/QJournal | cut -f1)"
    echo ""
    echo "To install system-wide, run: sudo ./install.sh"
    echo "To test locally, run: ./dist/QJournal"
    echo ""
else
    echo ""
    echo "Build failed! Check the output above for errors."
    exit 1
fi
