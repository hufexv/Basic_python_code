import scrapy
import json
from datetime import datetime
import time
from cloudmusic.items import CloudmusicItem

class MusicSpider(scrapy.Spider):
    name = 'music'
    allowed_domains = ['music.163.com/discover/toplist?id=3778678']
    start_urls = ['https://music.163.com/discover/toplist?id=3778678']

    def parse(self, response):
        # 获取榜单发布时间 time for list of songs
        update_time = response.css(".user span::text").extract()[0].strip().replace("最近更新：", "")

        # 获取包含歌曲信息的JSON数据
        str_data = response.css("textarea::text").extract()[0]

        with open("response.json", "w", encoding="utf-8") as file:
            file.write(str_data)

        json_data = json.loads(str_data)

        # 初始化一个列表来存储所有的歌曲信息
        songs_list = []

        # 遍历每首歌曲的信息，并按顺序生成序号
        for index, song_info in enumerate(json_data, start=1):  # start=1 表示从1开始计数
            # 获取发行时间，如果不存在则默认为2019-01-01
            if song_info.get('publishTime'):
                t1 = time.localtime(song_info.get('publishTime') / 1000)#timestamp->time_tuple
                publish_time = time.strftime("%Y-%m-%d %H:%M:%S", t1)#time_tuple->string
            else:
                publish_time = "2019-01-01"

            # 获取歌曲时长（单位：秒），原始数据是以毫秒为单位的
            song_time = song_info.get('duration') / 1000  # 计算歌曲时长（秒）
            song_time_min = str(int(song_time // 60))  # 计算分钟数
            song_time_sec = str(int(song_time % 60)).zfill(2)  # 计算秒数并补零
            song_time = f"{song_time_min}:{song_time_sec}"  # 组合时间格式

            # 获取所有歌手的名字，并用逗号连接起来
            artists_info = ', '.join([artist.get('name') for artist in song_info.get('artists', [])])  # 获取歌手名字list of string
            artist_id = ', '.join([str(artist.get('id')) for artist in song_info.get('artists', [])])  # 获取歌手 ID

            # 获取歌曲信息
            music_name = song_info.get('name')  # 歌名
            music_id = song_info.get('id')  # 音乐id

            # 构建歌曲下载地址和歌曲URL
            music_down_url = f"http://music.163.com/song/media/outer/url?id={music_id}.mp3"
            music_url = f"https://music.163.com/song?id={music_id}"

            # 获取专辑信息
            album = song_info.get('album').get('name')  # 专辑
            pic_url = song_info.get('album').get('picUrl')  # 专辑图url
            album_id = song_info.get('album').get('id')  # 专辑id

            # 获取爬取时间
            crawl_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            music_item = CloudmusicItem()
            music_item['no'] = index  # 使用列表的顺序作为排名信息
            music_item['music_name'] = music_name
            music_item['artist'] = artists_info
            music_item['publish_time'] = publish_time
            music_item['song_time'] = song_time
            music_item['artist_id'] = artist_id
            music_item['music_id'] = music_id
            music_item['album'] = album
            music_item['album_id'] = album_id
            music_item['pic_url'] = pic_url
            music_item['crawl_time'] = crawl_time
            music_item['music_url'] = music_url
            music_item['music_down_url'] = music_down_url
            music_item['update_time'] = update_time

            # 直接发送数据给Scrapy的管道
            yield music_item
