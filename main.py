import cv2
import os
import numpy as np
import videoUtil


def f2v(fps):
    src_frame_dir = './src_frame'
    gen_video_dir = './gen_video'
    for frame_set in os.listdir(src_frame_dir):
        frame_path = os.path.join(src_frame_dir, frame_set)  # 帧存放路径
        video_path = os.path.join(gen_video_dir, frame_set + str('.avi'))  # 合成视频存放的路径
        print("current video: %s\nfps:%d\nframe size:%d" % (video_path, fps, len(os.listdir(frame_path))))
        videoUtil.frame2video(frame_path, video_path, fps)  # fps :帧率，每秒钟帧数越多，所显示的动作就会越流畅


def v2f():
    video_dir = './src_video/'
    frame_dir = './gen_frame'
    for video_name in os.listdir(video_dir):
        if os.path.splitext(video_name)[1] == '.avi':
            video_path = os.path.join(video_dir, video_name)
            frame_path = os.path.join(frame_dir, os.path.splitext(video_name)[0])
            if not os.path.exists(frame_path):
                os.makedirs(frame_path)
            print(frame_path)
            videoUtil.video2frame(video_path, frame_path)


if __name__ == '__main__':
    # v2f()
    f2v(fps=50)
