from Filter import Filter
import cv2

class Rotator(Filter):

    def applyFilter(self, img):
        width, height = img.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
        rotated_image = cv2.warpAffine(img, rotation_matrix, (width, height))
        return rotated_image
