from Filter import Filter
import cv2


class MeanBlur(Filter):

    __kernelSize = (5,5)

    def setKernelSize(self, kernelSize):
        self.__kernelSize = kernelSize

    def getKernelSize(self):
        return self.__kernelSize

    def applyFilter(self, img):
        return cv2.blur(img, self.__kernelSize)


