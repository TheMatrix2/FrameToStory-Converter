import cv2
import random


def save_video(path_to_file, video_file):
    video = cv2.VideoCapture(video_file)
    # width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    # height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(video.get(cv2.CAP_PROP_FPS))

    output = cv2.VideoWriter(path_to_file, *'XVID', fps)


def frame_maker(videofile):
    video = cv2.VideoCapture(videofile)
    if not video.isOpened():
        return ValueError('Error: could not open video file')

    count_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    random_frame_number = random.randint(0, count_frames)
    video.set(cv2.CAP_PROP_POS_FRAMES, random_frame_number)

    ret, frame = video.read()
    video.release()

    if not ret:
        return ValueError('Error: could not read frame')

    return frame
