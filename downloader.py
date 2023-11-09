from pytube import YouTube

url = input("Enter video URL here: ")
yt = YouTube(url)

print("Title: ", yt.title)
print("Views: ", yt.views)
print("Description: ", yt.description)
print("Length: ", yt.length)
print("Publish Date: ", yt.publish_date)
print("Rating: ", yt.rating)

yd = yt.streams.get_highest_resolution()

yd.download()

print("Download complete.")