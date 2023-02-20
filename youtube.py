from pytube import YouTube

yt = YouTube("https://youtu.be/UyqnRW-CZs4")

stream = yt.streams.get_highest_resolution()

stream.download()