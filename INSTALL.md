# QJournal - Distribution Package

A privacy-focused personal journaling application built with PyQt6.

## Installation

### Linux

1. **Using the installation script (recommended):**
   ```bash
   sudo ./install.sh
   ```

2. **Manual installation:**
   - Copy the `QJournal` executable to a location of your choice
   - Make it executable: `chmod +x QJournal`
   - Run it: `./QJournal`

### What Gets Installed

- **Application**: `/opt/qjournal/QJournal`
- **Desktop Entry**: `/usr/share/applications/qjournal.desktop`
- **Command-line shortcut**: `/usr/local/bin/qjournal`

## Running QJournal

After installation, you can launch QJournal in three ways:

1. **From Application Menu**: Search for "QJournal" in your desktop environment's application launcher
2. **From Terminal**: Type `qjournal`
3. **Direct Execution**: Run `/opt/qjournal/QJournal`

## Data Storage

QJournal stores your data in platform-specific locations:

- **Linux**: `~/.config/QJournal/`
  - Database: `qJournal.db`
  - Configuration: `config.json`
  - Logs: `log.txt`

## Features

- 📝 Create and manage journal entries
- 😊 Track your daily mood
- 📅 Calendar view to browse entries by date
- 🔒 Encryption support for sensitive data
- ⌨️ Keyboard shortcuts (Ctrl+N for new entry, Ctrl+M for mood log)

## Uninstallation

To remove QJournal from your system:

```bash
sudo rm -rf /opt/qjournal /usr/share/applications/qjournal.desktop /usr/local/bin/qjournal
```

Your personal data in `~/.config/QJournal/` will be preserved. Delete it manually if desired.

## System Requirements

- Linux (64-bit)
- X11 or Wayland display server
- ~60MB disk space for the application
- Additional space for your journal data

## Support

For issues or questions, please visit the project repository.

## License

See LICENSE file for details.
