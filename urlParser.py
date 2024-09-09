import instagrapi as iApi
import moviepy.editor as mp
import pytubefix

import common
import voiceToText


def downloadYt(url):
    yt = pytubefix.YouTube(url)

    audStream = yt.streams.get_lowest_resolution()
    audStream.download(filename="test.mp4")

    video = mp.VideoFileClip("test.mp4")

    audio_file = video.audio
    audio_file.write_audiofile("test.wav")


def downloadInsta(url):
    cl = iApi.Client()
    accountName = "thxne__"
    accountPw = "thefirstredpanda"
    cl.login(accountName, accountPw)

    user_id = cl.user_id_from_username(accountName)
    medias = cl.user_medias(user_id, 10000000)

    formattedUrl = cl.media_info(
        cl.media_pk_from_url(url)).video_url
    cl.video_download_by_url(formattedUrl, filename="test")

    video = mp.VideoFileClip("test.mp4")

    audio_file = video.audio
    audio_file.write_audiofile("test.wav")


def urlParser(url):
    if url[0:8] != 'https://':
        url = "https://" + url
        print("string concantenated")

    print(url)

    if url[12:17] == "insta":
        print("instagram domain detected")
        common.changeLog("instagram domain detected")
        downloadInsta(url)
        common.changeLog("reel downloaded")
        voiceToText.voiceToText("test.wav")

    elif url[12:17] == "youtu":
        print("youtube domain detected")
        common.changeLog("youtube domain detected")
        downloadYt(url)
        common.changeLog("short downloaded")
        voiceToText.voiceToText("test.wav")


    else:
        print("no domain detected")
        common.changeLog("ERROR -> no domain detected")
