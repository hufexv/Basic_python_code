import pandas as pd

# 读取数据
data = pd.read_csv('output.csv')

# 将发布日期转换为日期时间类型
data['publish_time'] = pd.to_datetime(data['publish_time'], errors='coerce')

# 计算所有歌曲的平均发布时间
average_publish_time = data['publish_time'].mean()

# 获取前200首歌
data_top_200 = data.head(200)

# 统计发布大于平均发布时间和小于等于平均发布时间的歌曲
recent_songs = data_top_200[data_top_200['publish_time'] > average_publish_time]
old_songs = data_top_200[data_top_200['publish_time'] <= average_publish_time]

# 计算大于平均发布时间的平均排名（按数据顺序即"no"列）
recent_songs_average_rank = recent_songs.index.to_list()
old_songs_average_rank = old_songs.index.to_list()

# 计算排名的平均值
recent_songs_average_rank = sum(recent_songs_average_rank) / len(recent_songs_average_rank) + 1  # +1 因为 index 从0开始，需要转换为排名（从1开始）
old_songs_average_rank = sum(old_songs_average_rank) / len(old_songs_average_rank) + 1  # 同理

# 输出结果
print(f"发布大于平均发布时间的歌曲的平均排名：{recent_songs_average_rank:.2f}")
print(f"发布小于等于平均发布时间的歌曲的平均排名：{old_songs_average_rank:.2f}")
