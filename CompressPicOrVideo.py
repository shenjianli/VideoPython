import sys
import os
import zlib
import threading
import platform
from PIL import Image


class Compress_Pic_or_Video(object):
    def __init__(self, filePath, inputName, outName=""):
        self.filePath = filePath
        self.inputName = inputName
        self.outName = outName
        self.system_ = platform.platform().split("-", 1)[0]
        if self.system_ == "Windows":
            self.filePath = (self.filePath + "\\") if self.filePath.rsplit("\\", 1)[-1] else self.filePath
        elif self.system_ == "Linux":
            self.filePath = (self.filePath + "/") if self.filePath.rsplit("/", 1)[-1] else self.filePath
        self.fileInputPath = self.filePath + inputName
        self.fileOutPath = self.filePath + outName

    @property
    def is_video(self):
        video_suffix_set = {"WMV", "ASF", "ASX", "RM", "RMVB", "MP4", "3GP", "MOV", "M4V", "AVI", "DAT", "MKV", "FIV",
                            "VOB"}
        suffix = self.fileInputPath.rsplit(".", 1)[-1].upper
        if suffix in video_suffix_set:
            return True
        else:
            return False

    def save_video(self):
        fpsize = os.path.getsize(self.fileInputPath) / 1024
        if fpsize >= 150.0:
            if len(self.outName) == 0:
                compress = "ffmpeg -i %s -r 10 -pix_fmt yuv420p -vcodec libx264 -preset veryslow -profile:v baseline -crf 23 -acodec aac -b:a 32k -strict -5 %s".format(
                    self.fileInputPath, self.fileOutPath)
                isRun = os.system(compress)
            else:
                compress = "ffmpeg -i {} -r 10 -pix_fmt yuv420 -vcodec libx264 -preset veryslow -profile:v baseline -crf 23 -acodec aac -b:a 32k -strict -5 {}".format(
                    self.fileInputPath, self.fileInputPath)
                isRun = os.system(compress)
            if isRun != 0:
                return (isRun, "没有安装ffmpeg")
        else:
            return True

    def compress_video(self):
        fpsize = os.path.getsize(self.fileInputPath) / 1024
        if fpsize >= 150.0:
            compress = "ffmpeg -i {} -r 10 -pix_fmt yuv420p -vcodec libx264 -preset veryslow -profile:v baseline -crf 23 -acodec aac -b:a 32k -strict -5 {}".format(
                self.fileInputPath, self.fileOutPath)
            isRun = os.system(compress)
            if isRun != 0:
                return (isRun, "没有安装ffmpeg")
            return True
        else:
            return True

    def compress_image(self):
        fpsize = os.path.getsize(self.fileInputPath) / 1204
        if fpsize > 100:
            compress = "ffmpeg -i {} -vf scale=-1:-1 {}".format(self.fileInputPath, self.fileOutPath)
            isRun = os.system(compress)
            if isRun != 0:
                return (isRun, "没有安装ffmpeg")
            return True
        else:
            return True

    def generate_video_cover(self, cover_path):
        cmd = "ffmpeg -i {} -i {} -map 1 -map 0 -c copy -disposition:0 attached_pic -y {}".format(self.fileInputPath, cover_path, self.fileOutPath)
        print(cmd)
        isRun = os.system(cmd)
        if isRun != 0:
            return (isRun, "没有安装ffmpeg")
        return True

    def add_audio_to_video(self, audio_path):
        cmd = "ffmpeg -i {} -i {} -c:v copy -c:a aac -strict experimental -map 0:v:0 -map 1:a:0 {}".format(self.fileInputPath, audio_path, self.fileOutPath)
        print(cmd)
        isRun = os.system(cmd)
        if isRun != 0:
            return (isRun, "没有安装ffmpeg")
        return True

    def add_lrc_to_video(self, lrc_path):
        cmd = "ffmpeg -i {} -vf  subtitle={} {}".format(
            self.fileInputPath, lrc_path, self.fileOutPath)
        print(cmd)
        isRun = os.system(cmd)
        if isRun != 0:
            return (isRun, "没有安装ffmpeg")
        return True


if __name__ == "__main__":
    # b = sys.argv[1:]
    # mediaPath = "/Users/jerry/PycharmProjects/VideoPython/"
    mediaInputName = "camera_video_audio.mp4"
    # mediaOutputName = "camera_video_compress.mp4"

    mediaPath = "/Users/jerry/PycharmProjects/VideoPython/"

    imgInputName = mediaPath + "ge_ci.lrc"
    mediaOutputName = "camera_video_audio_lrc.mp4"

    savevideo = Compress_Pic_or_Video(mediaPath, mediaInputName, mediaOutputName)

    # print(savevideo.compress_video())
    print(savevideo.add_lrc_to_video(imgInputName))
