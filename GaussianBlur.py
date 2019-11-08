from Filter import Filter
import cv2


class GaussianBlur(Filter):
    def applyFilter(self, img):
        return cv2.GaussianBlur(img, (5, 5), 20)

