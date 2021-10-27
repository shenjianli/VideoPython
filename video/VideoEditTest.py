from moviepy.editor import *


# 视频旋转
def rotate_video():
    video_path = r'camera_video_audio.mp4'
    rotate_video_path = 'rotate_video.mp4'
    video = VideoFileClip(video_path)
    video = video.rotate(90)
    video.write_videofile(rotate_video_path)


# 调整视频中的音量
def adjust_video_audio():
    video_path = r'camera_video_audio.mp4'
    result_video_path = 'adjust_audio_video.mp4'
    video = VideoFileClip(video_path)
    # 声音放大3倍
    audio = video.audio.volumex(3)
    # 替换视频中的声音
    video = video.without_audio()
    result = video.set_audio(audio)
    result.write_videofile(result_video_path)


# 视频中颜色变换
def change_color_video():
    video_path = r'camera_video_audio.mp4'
    result_video_path = 'change_color_video.mp4'
    video = VideoFileClip(video_path)
    result = video.fl_image(lambda image: image[:, :, [1, 2, 0]])
    result.write_videofile(result_video_path)


# 调整视频播放速度
def add_speed_video():
    video_path = r'camera_video_audio.mp4'
    result_video_path = 'change_speed_video.mp4'
    video = VideoFileClip(video_path)
    result = video.fl_time(lambda t: 1.5*t, apply_to=['mask', 'video', 'audio']).set_end(video.end/1.5)
    result.write_videofile(result_video_path)


# 淡入淡出插入转场视频
def add_transition_video():
    video_path = r'camera_video_audio.mp4'
    result_video_path = 'transition_video.mp4'
    video = VideoFileClip(video_path)
    # 视频中0-20秒
    sub_video_1 = video.subclip(0, 20).fadein(3, (1, 1, 1)).fadeout(2, (1, 1, 1))
    # 视频中20-40秒
    sub_video_2 = video.subclip(20, 40).fadein(3, (1, 1, 1)).fadeout(2, (1, 1, 1))
    # 视频中40-结束
    sub_video_3 = video.subclip(40).fadein(3, (1, 1, 1)).fadeout(2, (0, 0, 0))

    transition = VideoFileClip(r'/转场视频.mp4').resize(video.size)

    result_video = concatenate_videoclips([sub_video_1, transition, sub_video_2, transition, sub_video_3])
    result_video.write_videofile(result_video_path)


# 增加淡入淡出并插入转场图片
def add_transition_img_video():
    video_path = r'camera_video_audio.mp4'
    result_video_path = 'transition_img_video.mp4'
    video = VideoFileClip(video_path)
    sub_video_1 = video.subclip(0, 20).fadein(3, (1, 1, 1)).fadeout(2, (1, 1, 1))
    sub_video_2 = video.subclip(20, 40).fadein(3, (1, 1, 1)).fadeout(2, (1, 1, 1))
    sub_video_3 = video.subclip(40).fadein(3, (1, 1, 1)).fadeout(2, (0, 0, 0))

    # 转场图片
    transition = ImageClip(r'big_pic_compress.jpeg', duration=2).resize(video.size)

    result_video = concatenate_videoclips([sub_video_1, sub_video_2, sub_video_3], transition=transition)
    result_video.write_videofile(result_video_path)



add_transition_img_video()