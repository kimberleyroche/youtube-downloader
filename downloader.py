from pytube import YouTube

url = input("Enter video URL here: ")
yt = YouTube(url)

print("Title: ", yt.title)
print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download()

print("Download complete.")