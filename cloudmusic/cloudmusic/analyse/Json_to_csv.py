import json
import pandas as pd
from datetime import datetime

# 文件路径
input_file = "D:\Thunder\cloudmusic\cloudmusic\spiders\\response.json"
output_file = "output.csv"

# 读取 JSON 文件
with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)

# 展平 JSON 数据
df = pd.json_normalize(data)

# 提取和转换字段
df_clean = pd.DataFrame({
    "publish_time": df.get("publishTime", 0).apply(lambda x: datetime.utcfromtimestamp(x / 1000).strftime('%Y-%m-%d') if x > 0 else "Unknown"),
    "song_time": df["duration"].apply(lambda x: f"{x // 60000}:{(x % 60000) // 1000:02}"),  # 转换为 MM:SS 格式
    "artist": df["artists"].apply(lambda x: ", ".join([artist["name"] for artist in x]) if isinstance(x, list) else "Unknown"),
    "artist_id": df["artists"].apply(lambda x: ", ".join([str(artist["id"]) for artist in x]) if isinstance(x, list) else "Unknown"),
    "music_name": df["name"],
    "music_id": df["id"],
    "album": df["album.name"],
    "pic_url": df["album.picUrl"],
    "album_id": df["album.id"],
    "no": df["no"],
    "crawl_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # 使用当前时间
    "music_url": df["id"].apply(lambda x: f"https://music.163.com/song?id={x}"),  # 拼接歌曲URL
    "music_down_url": None,  # 下载地址暂无数据来源
    "update_time": datetime.now().strftime('%Y-%m-%d')  # 使用当前日期作为榜单发布时间
})

# 缺失值处理
df_clean.fillna("Unknown", inplace=True)

# 导出到 CSV 文件
df_clean.to_csv(output_file, index=False, encoding="utf-8")

print(f"Data has been successfully converted to CSV and saved to {output_file}.")
