from Filter import Filter
import cv2

class Scaler(Filter):
    def applyFilter(self, img):
        return cv2.resize(img, None, fx =2, fy = 2, interpolation= cv2.INTER_CUBIC)