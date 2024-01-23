from bilibili_api import hot
from asyncio import run
from sys import argv

try:
    videos = int(argv[0])
except ValueError:
    videos = 20

result = run(hot.get_hot_videos(ps=videos))['list']
for video in result:
    print(f"Title: {video['title']} Author: {video['owner']['name']} Link: https://bilibili.com/video/av{video['aid']}")
