from os import listdir
from os.path import join
from re import findall
from moviepy.editor import *

pic_dir = r'img'
mp3_path = 'video_audio.mp3'
final_video_path = "img_to_video.mp4"
pic_files = [join(pic_dir, fn) for fn in listdir(pic_dir)
             if fn.endswith('.png')]
pic_files.sort(key=lambda fn: int(findall(r'\d+', fn)[-1]))

pic_num = len(pic_files)
print("图片个数：", pic_num)
mp3_clip = AudioFileClip(mp3_path)
mp3_clip = concatenate_audioclips([mp3_clip])
mp3_duration = mp3_clip.duration
each_duration = round(mp3_duration/pic_num, 2)
image_clips = []
for pic in pic_files:
    print("增加图片：", pic)
    image_clips.append(ImageClip(pic, duration=each_duration))

result_video = concatenate_videoclips(image_clips)
result_video = result_video.set_audio(mp3_clip)
# audio_codec 这个必须有，不然无法增加音频
result_video.write_videofile(final_video_path, fps=24, audio_codec='aac')