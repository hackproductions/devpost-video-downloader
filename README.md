# Devpost Video Downloader

This script will download all the videos inside of the Devpost CSV.

## Instructions
1. Download Devpost project data WITHOUT PII
2. Put this somewhere. Probably easiest inside the same folder as this script
3. Make sure `youtube-dl` is installed

## Setup
```
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
python downloader.py <csv_file_path>
```
