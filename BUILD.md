# QJournal Build & Distribution Guide

## Quick Start

### Building the Application

```bash
./build.sh
```

This will create a standalone executable at `dist/QJournal` (~60MB).

### Installing System-Wide

```bash
sudo ./install.sh
```

This installs QJournal to `/opt/qjournal` and creates desktop entries.

## Files Created

### Build Files
- `QJournal.spec` - PyInstaller specification file
- `build.sh` - Automated build script
- `install.sh` - System installation script
- `INSTALL.md` - User installation guide

### Output
- `dist/QJournal` - Standalone executable (single file, no dependencies needed)
- `build/` - Temporary build artifacts (can be deleted)

## Distribution

To distribute QJournal, package these files:

```
QJournal-dist/
├── QJournal           # The executable
├── install.sh         # Installation script
├── INSTALL.md         # Installation instructions
└── assets/            # Application icons (optional, for desktop entry)
    ├── qappicon.png
    └── journalsplash.png
```

Create a tarball:
```bash
tar -czf QJournal-v1.0-linux-x64.tar.gz dist/QJournal install.sh INSTALL.md assets/
```

## Technical Details

### PyInstaller Configuration

The `QJournal.spec` file includes:
- All Python dependencies bundled
- PyQt6 libraries included
- QSS stylesheets embedded
- Asset files (icons, images) packaged
- Single-file executable output
- No console window (GUI mode)

### Dependencies Bundled

- PyQt6 (GUI framework)
- SQLite3 (database)
- Cryptography (encryption)
- All Python standard libraries

### Platform Support

Currently configured for:
- **Linux x86_64** (tested)
- Can be adapted for Windows/macOS with spec file modifications

## Troubleshooting

### Build Issues

**Missing dependencies:**
```bash
pip install pyinstaller PyQt6 cryptography
```

**Permission errors:**
```bash
chmod +x build.sh install.sh
```

### Runtime Issues

**Missing libraries on target system:**
The executable is mostly self-contained, but may require:
- glibc 2.17+ (standard on modern Linux)
- X11 or Wayland display server

**Testing the executable:**
```bash
./dist/QJournal --help
```

## Development vs Distribution

### Development Mode
```bash
python main.py
```
- Runs from source
- Requires Python and dependencies installed
- Faster iteration for development

### Distribution Mode
```bash
./dist/QJournal
```
- Standalone executable
- No Python installation needed on target system
- Slower startup (unpacking overhead)
- Larger file size (~60MB vs ~100KB source)

## Future Improvements

- [ ] Create .deb package for Debian/Ubuntu
- [ ] Create .rpm package for Fedora/RHEL
- [ ] Add AppImage support for universal Linux distribution
- [ ] Windows .exe with installer
- [ ] macOS .app bundle
- [ ] Code signing for trusted distribution
- [ ] Auto-update mechanism

## Notes

- The executable includes all dependencies, so it's larger than the source
- First run may be slower as PyInstaller unpacks files
- User data is stored separately in `~/.config/QJournal/`
- The executable can be run from any location
