from moviepy.editor import *


# 获取视频中的音频信息
def get_audio_from_video():
    video_path = r'camera_video_audio.mp4'
    mp3_path = r'video_audio.mp3'
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(mp3_path)


# 删除视频中的音频
def delete_audio_from_video():
    video_path = r'camera_video_audio.mp4'
    silence_video_path = r'silence_video.mp4'
    video = VideoFileClip(video_path)
    video = video.without_audio()
    video.write_videofile(silence_video_path)


# 视频剪辑，拼接，添加字幕
# brew install imagemagick
# ImageMagick depends on Ghostscript fonts. To install them, type:
# brew install ghostscript
def video_clip_and_text():
    video_path_1 = r'camera_video_audio.mp4'
    video_path_2 = r'o_reader_test.mp4'
    final_path = r'final_video.mp4'
    # 剪切视频，从8s剪到2分30秒
    video1 = VideoFileClip(video_path_1).subclip(t_start=8, t_end=(2, 30))
    # 剪掉0到5秒
    video2 = VideoFileClip(video_path_2).cutout(0, 5)
    # 拼接两段视频
    video3 = concatenate_videoclips([video2, video1])
    # 创建并添加，合成字幕
    text_clip = TextClip(txt='Jerry专属', fontsize=50, color='black', bg_color='transparent', transparent=True).set_position(('right', 'top')).set_duration(30).set_start(0)
    video = CompositeVideoClip([video3, text_clip])
    video.write_videofile(final_path)


# 倒放视频
def end_to_start_video():
    video_path_1 = r'demo_test.mp4'
    result_video_path = r'end_to_start_video.mp4'
    video = VideoFileClip(video_path_1)
    video.subclip(t_start=0.1, t_end=-0.1).fx(vfx.time_mirror).write_videofile(result_video_path, codec='libx264')
    #video.subclip(t_start=0.1).fx(vfx.time_mirror).write_videofile(result_video_path, codec='libx264')


# 视频添加字幕
def add_audio_text_video():
    video_path = r'camera_video_audio.mp4'
    final_path = r'add_audio_text_video.mp4'
    video = VideoFileClip(video_path)

    # 逐句出现的字幕
    sentences = [('我们这个视频，主要演示怎么样添加字幕', 4, 7),
                 ('如何设置上边距和左边距不同', 12, 7),
                 ('margin的值为1个，2个，3个，4个数值是分别表示什么含义', 32, 11)]

    # 逐词出现的字幕
    words = [('下面', 28, 3),
             ('开始', 28.5, 2.5),
             ('加字幕', 29, 2)]
    txts = []

    # 逐句添加字幕，居中对齐
    for sentence, start, span in sentences:
        txt = (TextClip(sentence, fontsize=40,
                        size=(1200, 40),
                        align='center', color='black')
               .set_position((10, 60))
               .set_duration(span).set_start(start))
        txts.append(txt)

    # 逐词出现加字幕，left为起始位置
    left = 80
    for index, (word, start, span) in enumerate(words):
        width = 40*len(word)
        txt = (TextClip(word, fontsize=40,
                        size=(width, 40),
                        align='center', color='black')
               .set_position((left, 60))
               .set_duration(span).set_start(start))
        txts.append(txt)
        left = left + width

    video_clip = [video, *txts]
    print("video_clip = ", video_clip)
    video = CompositeVideoClip(video_clip)
    video.write_videofile(final_path, fps=24)


from os.path import splitext,isfile


'''
pip install moviepy 1.0.0
pip install imageio
pip install imageio-ffmpeg
另外，需要单独安装ImageMagick软件，并把安装路径添加到path变量中
'''
# 根据txt文本增加字幕
def normal_audio_text_video():
    src_video = r'camera_video_audio.mp4'
    txt_sentence = r'sentence.txt'
    if not (isfile(src_video) and src_video.endswith(('.avi','mp4')) and isfile(txt_sentence) and txt_sentence.endswith('.txt')):
        print('请正确使用本程序')
    else:
        video = VideoFileClip(src_video)
        w, h = video.w, video.h
        txts = []
        with open(txt_sentence, encoding='utf8') as fp:
            for line in fp:
                txt_sentence, stat, span = line.split(':')
                print(txt_sentence, stat, span)
                stat, span = map(float, (stat, span))
                txt = (TextClip(txt_sentence, fontsize=40, size=(w - 20, 40), align='center', color='black')
                       .set_position((10, h-150))
                       .set_duration(span).set_start(stat))
                txts.append(txt)
        video = CompositeVideoClip([video, *txts])
        fn, ext = splitext(src_video)
        video.write_videofile(f'{fn}_text_jerry{ext}')


normal_audio_text_video()