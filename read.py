import cv2 as cv
import time
import sys


class ReadVideoFile:

    def __init__(self, files):
        self.files = files

    def __del__(self):
        self.files.clear()


    def play(self):
        for fname in self.files:
            cap = cv.VideoCapture(fname)
            print(fname)
            if not cap.isOpened():
                print("Error opening video file")
                exit(0)

            print("Video properties")
            print("Video Dimensions: ", cap.get(cv.CAP_PROP_FRAME_WIDTH), cap.get(cv.CAP_PROP_FRAME_HEIGHT) )
            print("Video FPS: ", cap.get(cv.CAP_PROP_FPS) )

            while( cap.isOpened() ):
                ret, img = cap.read()
                if ret:
                    imgin = img[:, :, (0, 1, 2)]
                else:
                    break

                cv.imshow( "camOut", img )
                cv.waitKey( 1 )
                time.sleep( 1 / cap.get(cv.CAP_PROP_FPS) )

            cap.release()
         

if __name__ == '__main__':
    rvf = ReadVideoFile(sys.argv[1:])
    rvf.play()
