from scipy import ndimage
import cv2

#img = ndimage.imread("/home/paul/Documents/SC/sharpness/high.png")

def getMaxLap(path):


    srcImg = cv2.cv.LoadImage(path)

    srcImg = cv2.imread(path)

    #srcImg = cv2.imread("/home/paul/Documents/SC/sharpness/high.png")

    destImg = cv2.cv.CreateImage((426,418), cv2.IPL_DEPTH_16S, 3)



    #cv2.cv.Laplace(srcImg, cv2.CV_64F)
    maxLap = cv2.Laplacian(srcImg, cv2.CV_64F).var()
    #print destImg.var()



    # maxLap = -32767
    # print dir(destImg)
    # data = destImg.tostring()
    #
    # for i in data:
    #
    #     # for j in range(426):
    #     #     print j
    #     print float(i)
    #
    #     if i > maxLap:
    #
    #         maxLap = i
    #
    return maxLap





#print getBlurFactor("/home/paul/Documents/SC/sharpness/high.png")
#print getBlurFactor("/home/paul/Documents/SC/sharpness/medium.png")
#print getBlurFactor("/home/paul/Documents/SC/sharpness/low.png")


class LaserFocus(object):

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.max_focus = float('-Inf')

    def updateMaxFocus(self, blur):
        """
        update a second line on the lcd if it is possible
        """
        pass

    def showMaxFocus(self):
        """
        show a light is close to max focus
        """
        pass

    def hideMaxFocus(self):
        """
        show a light is close to max focus
        """
        pass

    def inMaxFocus(self, blur):
        if abs(blur - self.max_focus) < 2.0:
            return True
        return False

    def begin(self):

        try:
            while(True):
                # Capture frame-by-frame
                ret, frame = self.cap.read()

                # Our operations on the frame come here

                #print frame
                frameBlur = self.getBlurFactor(img=frame)
                if frameBlur > self.max_focus:
                    self.max_focus = frameBlur
                if self.inMaxFocus(frameBlur):
                    self.showMaxFocus()
                    self.updateMaxFocus(frameBlur)

                # Display the resulting frame
                #cv2.imshow('frame',gray)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        except KeyboardInterrupt:
            pass
        except Exception, e:
            print "Error: %s" % str(e)
        self.cleanup()

    def getBlurFactor(self, img=None, path=None):
        if path:
            img = cv2.imread(path)
        return cv2.Laplacian(img, cv2.CV_64F).var()

    def cleanup(self):

        print "releasing"
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    #LF = LaserFocus()
    #LF.begin()

    cap = cv2.VideoCapture(1)

    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        print cv2.Laplacian(frame, cv2.CV_64F).var()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()






