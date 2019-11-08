from Filter import Filter
import cv2


class MedianBlur(Filter):
    def applyFilter(self, img):
        return cv2.medianBlur(img, 5)


