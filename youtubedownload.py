import pytube
video_link="https://www.youtube.com/watch?v=7E1M1W9o7PA&list=PLsyeobzWxl7r2ukVgTqIQcl-1T0C2mzau&index=15"
yt=pytube.YouTube(video_link)
videos=yt.streams.first()
videos.download("D://pyhtno")