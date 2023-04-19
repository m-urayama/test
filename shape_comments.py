import sys
import json
import pandas as pd

def round_elapsed_time(elapsed_time):
    ts = elapsed_time.split(":")
    length = len(ts)
    min = 0
    if length == 1:
        min = 0
    elif length == 2:
        min = int(ts[0])
    elif length == 3:
        min = int(ts[0]) * 60 + int(ts[1])
    return min

args = sys.argv
video_id = args[1]

with open(f"./comments/{video_id}.json", mode="r", encoding="utf-8") as f:
    comments = f.read()

comments = json.loads(comments)

comments = {"json_col": comments}
df = pd.DataFrame(comments)
df_json = pd.io.json.json_normalize(df["json_col"].apply(lambda x: x))
df_ts = df_json.loc[:,["id","timestamp","elapsedTime","message"]]
print(df_ts.head())
print(f"コメント数：{len(df_ts)}")
df_elapsed = df_json[["elapsedTime"]]
# NOTE: これを0, 1, 2って分ごとにまとめてヒストグラムを出す
df_min = df_elapsed.applymap(lambda x: round_elapsed_time(x))
df_min.elapsedTime.value_counts().sort_index().plot.bar(figsize = (200, 4)).get_figure().savefig(f"./comments/{video_id}.png")


