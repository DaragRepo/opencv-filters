from Filter import Filter
import cv2
import numpy as np
import numpy as np
import matplotlib.pyplot as plt

class Histogram(Filter):
    def applyFilter(self, img):
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            histogram = cv2.calcHist([img], [i], None, [256], [0, 256])
            plt.plot(histogram, color=col)
        plt.xlim([0, 256])
        plt.show()
