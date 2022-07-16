import cv2 as cv
import time
import sys
import os


class ReadVideoFile:
    def __init__(self, directory_path = os.path.abspath(os.getcwd())):
        self.directory_path = directory_path
        #self.extensions = ['.dvi', '.mp4']
        self.extensions = ['.dvi']
        self.checkDiractory()
        self.filtered_files = []

    def __del__(self):
        self.filtered_files.clear()

    def createDirectory(self, folder = 'MP4Videos'):
        isExist = os.path.exists(self.directory_path + '/' + folder)
        if not isExist:
            os.makedirs(self.directory_path + '/' + folder)

    def checkDiractory(self):
        if os.path.isdir(self.directory_path) == False:
            print('The specified directory does not exist.')
            exit()

    def getFilteredFiles(self):
        self.filtered_files = list()
        for fname in os.listdir(self.directory_path):
            if fname[-4:] in self.extensions:
                self.filtered_files.append(fname)                
        self.filtered_files.sort()


    def play(self):
        self.getFilteredFiles()

        for fname in self.filtered_files:
            cap = cv.VideoCapture(fname)
            if not cap.isOpened():
                continue

            while( cap.isOpened() ):
                ret, frame = cap.read()
                if ret:
                    frame = frame[:, :, (0, 1, 2)]
                    cv.imshow( "camOut", frame )
                    cv.waitKey( 1 )
                    time.sleep( 1 / cap.get(cv.CAP_PROP_FPS) )
                else:
                    break

            cap.release()
        cv.destroyAllWindows()

    def convertToAVI(self):
        folder = 'MP4Videos'
        self.createDirectory( folder=folder )
        self.getFilteredFiles()

        for fname in self.filtered_files:
            cap = cv.VideoCapture(self.directory_path + '/' + fname)
            if not cap.isOpened():
                continue
            
            filename = fname.replace(fname[-4:],'.avi')
            fourcc = cv.VideoWriter_fourcc(*'XVID')
            fps = 20.0
            frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
            frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
            resolution = (frame_width, frame_height)
            outputVideo = cv.VideoWriter(
                    self.directory_path + '/' + folder + '/' + filename, 
                    fourcc, 
                    fps, 
                    resolution)

            while( cap.isOpened() ):
                ret, frame = cap.read()
                if ret == True:
                    outputVideo.write(frame)
                    if cv.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break

            cap.release()
            outputVideo.release()

        cv.destroyAllWindows()


    def convertToMP4(self):
        folder = 'MP4Videos'
        self.createDirectory( folder=folder )
        self.getFilteredFiles()

        for fname in self.filtered_files:
            cap = cv.VideoCapture(self.directory_path + '/' + fname)
            if not cap.isOpened():
                continue
            
            filename = fname.replace(fname[-4:],'.mp4')
            fourcc = cv.VideoWriter_fourcc(*'mp4v')
            fps = 20.0
            frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
            frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
            resolution = (frame_width, frame_height)
            outputVideo = cv.VideoWriter(
                    self.directory_path + '/' + folder + '/' + filename, 
                    fourcc, 
                    fps, 
                    resolution)

            while( cap.isOpened() ):
                ret, frame = cap.read()
                if ret == True:
                    #imgin = frame[:, :, (0, 1, 2)]

                    outputVideo.write(frame)

                    #cv.imshow( "camOut", frame )
                    #cv.waitKey( 1 )
                    #time.sleep( 1 / cap.get(cv.CAP_PROP_FPS) )

                    if cv.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break

            cap.release()
            outputVideo.release()

        cv.destroyAllWindows()

        

if __name__ == '__main__':

    path = ''
    if len(sys.argv) == 1:
        path = os.path.abspath(os.getcwd())
    else:
        path = sys.argv[1]

    print(path)

    rvf = ReadVideoFile(path)
    rvf.convertToMP4()
