# QJournal

An advanced journaling application built with PyQt6.

## Features

- **First-time setup**: Guided setup process for new users
- **Main interface**: Clean calendar-based journal interface
- **New entries**: Create and manage journal entries
- **Settings**: Configure application preferences
- **Cloud sync**: Support for multiple cloud storage providers (planned)

## Requirements

- Python 3.8+
- PyQt6 >= 6.0.0
- sqlite3

## Installation

1. Clone the repository:
```bash
git clone https://github.com/scutoidzz/QJournal.git
cd QJournal
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

## Project Structure

```
QJournal/
├── main.py                 # Application entry point
├── mainapp/               # Main application logic
├── newentry/              # New entry creation
├── settings/              # Application settings
├── firsttimesetup/        # First-time setup
├── splash/               # Splash screen
├── encryption/           # Encryption utilities
├── functions/            # Utility functions
├── cloud/               # Cloud sync functionality
└── assets/              # Application assets
```

## Usage

1. **First run**: The application will guide you through initial setup
2. **Main view**: View your journal entries by date using the calendar
3. **New entry**: Click "New Entry" to create a new journal entry
4. **Settings**: Configure cloud sync and other preferences

## Development

This project uses PyQt6 for the GUI and SQLite for data storage. The codebase has been cleaned up to provide a bare-bones foundation for further development.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License
