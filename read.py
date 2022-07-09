import cv2 as cv
import time
import sys

if __name__ == '__main__':

    video_file_name = sys.argv[1]

    cap = cv.VideoCapture(video_file_name)

    if not cap.isOpened():
        print("Error opening video file")
        exit(0)

    print("Video properties")
    print("Video Dimensions: ", cap.get(cv.CAP_PROP_FRAME_WIDTH), cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    print("Video FPS: ", cap.get(cv.CAP_PROP_FPS))

    while( cap.isOpened() ):
        ret, img = cap.read()
        if ret:
            imgin = img[:, :, (0, 1, 2)]
        else:
            break

        cv.imshow("camOut", img)
        cv.waitKey(1)
        time.sleep(1/cap.get(cv.CAP_PROP_FPS))


    cap.release()
    
