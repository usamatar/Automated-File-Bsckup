import os
import shutil
import datetime
import schedule
import time

# Define source and destination directories
source_dir = r"C:\Users\Dell\Pictures\Screenshots"
destination_dir = r"C:\Users\Dell\Desktop\Backup"

def backup(source, destination):
    today = datetime.date.today()
    destination_path = os.path.join(destination, str(today))  # Use correct variable name

    try:
        shutil.copytree(source, destination_path)
        print(f"Backup created successfully at {destination_path}")
    except FileExistsError:
        print("Backup already exists")

# Schedule the backup function to run every day at 2 AM
schedule.every().day.at("02:00").do(backup, source_dir, destination_dir)

print("Backup scheduling started. Press Ctrl+C to stop.")

# Keep the script running to execute the scheduled task
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait for a minute before checking again
