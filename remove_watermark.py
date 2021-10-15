import cv2
import numpy as np
from PIL import Image, ImageEnhance

def is_gray(a, b, c):
    r = 60
    if a + b + c < 250:
        return True
    if abs(a - b) > r:
        return False
    if abs(a - c) > r:
        return False
    if abs(b - c) > r:
        return False
    return True


def remove_watermark(image):
  "Replace watermark value color RGB to White"
  
    image = Image.convert("RGB")
    color_data = Image.getdata()

    new_color = []
    for item in color_data:
        if is_gray(item[0], item[1], item[2]):
            new_color.append(item)
        else:
            new_color.append((255, 255, 255))

    image.putdata(new_color)
//    img = np.array(image)
// cv2.imwrite("data_test/result/result.png",img[:, :, ::-1])
    return image

def remove_v2(image):
    """Use contrast in ImageEnhance
    """
    image = Image.fromarray(image)
    image_contrast = ImageEnhance.Contrast(image).enhance(1.5)

    img_hsv = cv2.cvtColor(np.array(image_contrast)[:, :, ::-1],
                            cv2.COLOR_BGR2HSV)

    red_lower = np.array([110, 50, 50], np.uint8)
    red_upper = np.array([200, 255, 255], np.uint8)
    red_mask = cv2.inRange(img_hsv, red_lower, red_upper)

    kernal = np.ones((5, 5), "uint8")
    red_mask = cv2.dilate(red_mask, kernal)

    dst = cv2.inpaint(img, red_mask, 0 , cv2.INPAINT_TELEA)

    return dst
