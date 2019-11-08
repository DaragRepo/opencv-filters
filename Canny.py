from Filter import Filter
import cv2
import numpy as np

class Canny(Filter):
    def applyFilter(self, img):
        canny = cv2.Canny(img,200,200)
        cv2.imshow('Canny', canny)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return img