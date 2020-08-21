import os
from datetime import datetime

s = ''
videos = os.listdir('/home/pi/Videos/Newvids')
videos.sort()
sorted(videos)
for video in videos:
    if video.endswith(".mp4"):
        s += ('file \'/home/pi/Videos/Processing/'+video+'\' \n')
	os.system('mv ~/Videos/Newvids/'+video+' ~/Videos/Processing')
print(s)
video_to_stitch = open('Videos/videos.txt', 'w')
u = video_to_stitch.write(s)
video_to_stitch.close()
now = datetime.now()
dt_string = now.strftime("%d_%m_%Y_%H:%M:%S")
concatCMD = ('ffmpeg -f concat -safe 0 -i Videos/videos.txt -c copy outputs/output'+dt_string+'.mp4')
os.system(concatCMD)
os.system('mv ~/Videos/Processing/* ~/Videos/Trash')
os.system('python push.py')
