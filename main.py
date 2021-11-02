import cv2
import os
import numpy as np
import videoUtil

if __name__ == '__main__':
    frame_path = 'datasets/LR/'  # 帧存放路径
    video_path = 'result/1.avi'  # 合成视频存放的路径
    fps = 50  # 帧率，每秒钟帧数越多，所显示的动作就会越流畅
    videoUtil.frame2video(frame_path, video_path, fps)

    # video_path = 'v_ApplyEyeMakeup_g05_c01.avi'
    # frame_path = './video2frame'
    # videoUtil.video2frame(video_path,frame_path)
