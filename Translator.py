from Filter import Filter
import cv2
import numpy as np

class Translator(Filter):
    def applyFilter(self, img):
        width, height = img.shape[:2]
        T = np.float32([[1,0, 200],[0, 1, 50]])
        translated = cv2.warpAffine(img, T, (width, height))
        return translated
