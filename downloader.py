import os
import sys
import pandas as pd

def collect_urls(csv_file):

    df = pd.read_csv(csv_file)
    urls = df['Video Demo Link'].tolist()

    for url in urls:
        os.system(f"youtube-dl {url}")
    print("Videos downloaded")


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        collect_urls(args[1])
