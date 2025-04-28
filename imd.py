
import os
from pathlib import Path
from datetime import datetime, timezone, timedelta
from shutil import copy2  

SOURCE = Path("/data/data/com.instagram.android/cache/images.stash/clean")
TARGET = Path("/storage/emulated/0/Pictures/Instagram")
MIN_SIZE = 1024 * 50  # 50KB

TIME = int(input("From how many hours ago to download? (hours) "))
threshold = datetime.now(timezone.utc) - timedelta(hours=TIME)

def main():
    if not SOURCE.exists():
        print(f"Error: Source directory doesn't exist: {SOURCE}")
        return

    TARGET.mkdir(parents=True, exist_ok=True)
    
    copied_files = 0
    for filename in os.listdir(SOURCE):
        source_file = SOURCE / filename
        
        try:
            if source_file.stat().st_size < MIN_SIZE:
                continue
            if filename.startswith(("htt", "igcdn")):
                continue
            if datetime.fromtimestamp(source_file.stat().st_mtime, timezone.utc) < threshold:
                continue
            
            clean_name = filename.split("==")[0] + ".jpg"
            target_file = TARGET / clean_name
            
            copy2(source_file, target_file)
            copied_files += 1
            
            print(f"Copied: {filename} → {clean_name}")
            
        except Exception as e:
            print(f"Error copying {filename}: {e}")

    print(f"\nCopied {copied_files} files to {TARGET}")

if __name__ == "__main__":
    main()
