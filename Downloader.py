import os
from pytube import Playlist
from pytube import YouTube, streams

option = int(input('1 = Audio Playlist;\n2 = Audio/Music;\n3 = Video;\n4 = Video Playlist.\nChoose one: '))
count = 0

if option == 1:
    link = input('Insert the URL: ')
    yt = Playlist(link)
    for url in yt.video_urls:
        count = count + 1
        ys = YouTube(url)
        print('%iº Title -' % count, ys.title)
        v = ys.streams.get_audio_only()
        out_file = v.download(rf'Your local file.')
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
    print('Finished Downloads.')

elif option == 2:
    url = str(input("Insert the URL: "))
    yt = YouTube(url)
    print('Title -', yt.title)
    video = yt.streams.filter(only_audio=True).first()
    downloaded_file = video.download(rf'Your local file.')
    base, ext = os.path.splitext(downloaded_file)
    new_file = base + '.mp3'
    os.rename(downloaded_file, new_file)
    print("Finished download.")

elif option == 3:
    url = input(str("Insert the URL: "))
    video = YouTube(url)
    print('Title -', video.title)
    stream = video.streams.get_highest_resolution()
    stream.download(output_path=rf'Your local file.')
    print('Finished download.')

elif option == 4:
    link = input('Insert the URL: ')
    yt = Playlist(link)
    for url in yt.video_urls:
        count = count + 1
        ys = YouTube(url)
        print('%iº Title -' % count, ys.title)
        stream = ys.streams.get_highest_resolution()
        out_file = stream.download(rf'Your local file.')
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp4'
        os.rename(out_file, new_file)
    print('Finished Downloads.')

else:
    print('Error.')