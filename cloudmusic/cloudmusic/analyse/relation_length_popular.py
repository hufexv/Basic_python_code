import pandas as pd

# 读取数据
data = pd.read_csv('output.csv')

# 将歌曲时长转换为秒数
data['song_time_seconds'] = data['song_time'].apply(
    lambda x: sum(int(i) * 60 ** idx for idx, i in enumerate(x.split(":")[::-1])) if isinstance(x, str) and ':' in x else 0
)

# 计算所有歌曲的平均时长
average_song_time = data['song_time_seconds'].mean()

# 获取前200首歌
data_top_200 = data.head(200)

# 统计大于平均时长和小于等于平均时长的歌曲
long_songs = data_top_200[data_top_200['song_time_seconds'] > average_song_time]
short_songs = data_top_200[data_top_200['song_time_seconds'] <= average_song_time]

# 计算大于平均时长的平均排名（按数据顺序即"no"列）
long_songs_average_rank = long_songs.index.to_list()
short_songs_average_rank = short_songs.index.to_list()

# 计算排名的平均值
long_songs_average_rank = sum(long_songs_average_rank) / len(long_songs_average_rank) + 1  # +1 因为 index 从0开始，需要转换为排名（从1开始）
short_songs_average_rank = sum(short_songs_average_rank) / len(short_songs_average_rank) + 1  # 同理

# 输出结果
print(f"average length: {average_song_time}")
print(f"number of long songs:{len(long_songs)}")
print(f"number of short songs:{len(short_songs)}")
print(f"average rank for long song：{long_songs_average_rank:.2f}")
print(f"average rank for short song：{short_songs_average_rank:.2f}")
