import numpy as np
import cv2


class BasicOperations():

    def __init__(self, image):
        super().__init__()
        self.image = image

    # rotate operations 90 - 180 - 270
    def rotate_image_90(self):
        new_image = cv2.rotate(self.image, cv2.cv2.ROTATE_90_CLOCKWISE)
        return new_image

    def rotate_image_180(self):
        new_image = cv2.rotate(self.image, cv2.cv2.ROTATE_180)
        return new_image

    def rotate_image_270(self):
        new_image = cv2.rotate(self.image, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
        return new_image

    # flipping operations vertical - horizontal - vertical & horizontal
    def flip_image_vertical(self):
        new_image = cv2.flip(self.image, 0)
        return new_image

    def flip_image_horizontal(self):
        new_image = cv2.flip(self.image, 1)
        return new_image

    def flip_image_horizontal_vertical(self):
        new_image = cv2.flip(self.image, -1)
        return new_image

    # --- New Functions can be added under here ---#
