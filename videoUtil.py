import cv2
import os
import numpy as np


def video2frame(video_path, frame_path):
    capture = cv2.VideoCapture(video_path)
    flag, frame = capture.read()
    i = 0
    while flag:
        flag, frame = capture.read()
        if not flag:
            break
        fileName = "image%d.jpg" % i
        i += 1
        print(os.path.join(frame_path, fileName))
        res = cv2.imwrite(os.path.join(frame_path, fileName), frame)


def frame2video(frame_path, video_path, fps):
    frame_list = os.listdir(frame_path)
    img = cv2.imread(os.path.join(frame_path, frame_list[0]))
    print('img size' + str(img.shape[:2]))
    frameSize = img.shape[:2][::-1]
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    '''frameSize和img shape的关系'''
    videoWriter = cv2.VideoWriter(video_path, fourcc, fps, frameSize=frameSize)
    for i, frame in enumerate(frame_list):
        # print("processing: %d/%d" % (i + 1, len(frame_list)))
        frame_name = os.path.join(frame_path, frame)
        img = cv2.imread(frame_name)

        videoWriter.write(img)
    videoWriter.release()


if __name__ == '__main__':
    frame_path = 'datasets/evaluations/vid4/TMNet/walk/'  # 帧存放路径
    video_path = 'src_video/test.avi'  # 合成视频存放的路径
    fps = 30  # 帧率，每秒钟帧数越多，所显示的动作就会越流畅
    frame2video(frame_path, video_path, fps)
