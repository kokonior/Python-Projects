from pytube import youtube 
link = input("Enter Url:")
video = youtube(link)
stream = video.stream.get_highest_resolution()
stream.download()