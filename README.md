# Automated Backup Script

## Overview
This Python script automatically creates a backup of files from a specified source directory to a destination directory every day at 2 AM. It uses the `schedule` module to manage automated execution.

## Features
- Backs up files from the source directory to a daily timestamped folder.
- Runs automatically at the scheduled time.
- Prevents duplicate backups for the same day.

## Requirements
Ensure you have the following installed:
- Python 3.x
- Required modules: `os`, `shutil`, `datetime`, `schedule`, `time`

You can install missing modules using:
```bash
pip install schedule
```

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/backup-script.git
   cd backup-script
   ```
2. Update the script with your desired source and destination directories:
   ```python
   source_dir = r"C:\Users\Dell\Pictures\Screenshots"
   destination_dir = r"C:\Users\Dell\Desktop\Backup"
   ```
3. Run the script:
   ```bash
   python backup_script.py
   ```
4. The script will run in the background and execute the backup daily at 2 AM.

## Stopping the Script
To stop the script, press `Ctrl+C` in the terminal where it is running.



