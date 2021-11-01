import cv2
import os
import numpy as np


def video2frame(video_path, frame_path):
    capture = cv2.VideoCapture(video_path)
    flag, frame = capture.read()
    i = 0
    while flag:
        flag, frame = capture.read()
        fileName = "image%d.jpg" % i
        i += 1
        res = cv2.imwrite(os.path.join(frame_path, fileName), frame)


def frame2video(frame_path, video_path, fps):
    frame_list = os.listdir(frame_path)
    img = cv2.imread(frame_path+frame_list[0])
    print(img.shape[:2])
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    videoWriter = cv2.VideoWriter(video_path, fourcc, fps,frameSize = img.shape[:2])
    for frame in frame_list:
        frame_name = os.path.join(frame_path, frame)
        img = cv2.imread(frame_name)
        # cv2.imshow('image',img)
        # cv2.waitKey(0)
        frame = cv2.imread(np.fromfile(frame_name, dtype=np.uint8), -1)
        videoWriter.write(img)
    videoWriter.release()


if __name__ == '__main__':
    frame_path = 'evaluations/vid4/TMNet/walk/'  # 帧存放路径
    video_path = 'test.mp4'  # 合成视频存放的路径
    fps = 30  # 帧率，每秒钟帧数越多，所显示的动作就会越流畅
    frame2video(frame_path, video_path, fps)
