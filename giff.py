from moviepy.editor import *

video_clip = VideoFileClip("task_01.mp4")
video_clip = video_clip.subclip(2,8)
video_clip.write_gif("Task_01.gif",fps = 10)
gif_video_clip = VideoFileClip("Task_01.gif")
gif_video_clip.ipython_display()