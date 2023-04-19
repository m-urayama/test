import pytchat
import time
import sys

args = sys.argv
video_id = args[1]
chat = pytchat.create(video_id=video_id)

all_comments = ""

while chat.is_alive():
    comments = chat.get().json().encode("utf-8").decode('utf-8')
    all_comments = all_comments + comments
    time.sleep(5)

all_comments = all_comments[:-2].replace("][", ", ")

with open(f"./comments/{video_id}.json", mode="w", encoding="utf-8") as f:
    f.write(all_comments)