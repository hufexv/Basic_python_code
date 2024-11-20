import pandas as pd
from matplotlib import pyplot as plt, rcParams
from matplotlib.font_manager import FontProperties

# 设置支持中文的字体
font_path = "C:/Windows/Fonts/simhei.ttf"  # 微软黑体字体路径（Windows 系统）
font_prop = FontProperties(fname=font_path)
rcParams["font.family"] = font_prop.get_name()

# 如果需要，禁用负号显示问题（仅中文场景需要）
plt.rcParams["axes.unicode_minus"] = False

# 读取数据
data = pd.read_csv('output.csv')

# 统计每个歌手的出现次数
artist_counts = data['artist'].value_counts()

# 只取前20个歌手
top_20_artists = artist_counts.head(20)

# 绘制饼图
plt.figure(figsize=(8, 8))
plt.pie(top_20_artists, labels=top_20_artists.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('popularity_top20', fontproperties=font_prop)
plt.axis('equal')  # 确保饼图是圆形的
plt.tight_layout()
plt.show()
