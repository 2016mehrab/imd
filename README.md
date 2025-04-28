# Instagram Image Downloader

Grab images from Instagram's cache.

## Requirements
- Python 3.6+
- Android with Termux with root 
- Must view the images in instagram that needs to be grabbed

## Usage
1. Save script as `instagram_downloader.py`.
2. Run:
   ```bash
   python instagram_downloader.py
   ```
3. Enter hours to filter images (e.g., `24` for last 24 hours).
4. Images are copied to `/storage/emulated/0/Spicy/Pictures/Instagram`.

## Notes
- Run in Termux with root.
- Source path requires Instagram app cache access.