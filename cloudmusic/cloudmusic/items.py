# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class CloudmusicItem(scrapy.Item):
    publish_time = scrapy.Field()     # 歌曲发布时间
    song_time = scrapy.Field()        # 歌曲时长，格式为 MM:SS
    artist = scrapy.Field()           # 歌手
    artist_id = scrapy.Field()        # 歌手id
    music_name = scrapy.Field()       # 歌名
    music_id = scrapy.Field()         # 音乐id
    album = scrapy.Field()            # 专辑
    pic_url = scrapy.Field()          # 专辑封面图url
    album_id = scrapy.Field()         # 专辑id
    no = scrapy.Field()               # 本周排名
    crawl_time = scrapy.Field()       # 爬取时间
    music_url = scrapy.Field()        # 歌曲url
    music_down_url = scrapy.Field()   # 音乐下载地址
    update_time = scrapy.Field()      # 榜单发布时间
