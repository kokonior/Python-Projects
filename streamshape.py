# USAGE
# python detect_shapes.py --image shapes_and_colors.png

# import the necessary packages
import argparse
import imutils
from cv2 import cv2

# initiate the videocapture
cap = cv2.VideoCapture(0)

# function for detecting shapes


def detectshape(c):
    # initialize the shape name and approximate the contour
    shape = "unidentified"
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)

    # if the shape is a triangle, it will have 3 vertices
    if len(approx) == 3:
        shape = "triangle"

    # if the shape has 4 vertices, it is either a square or
    # a rectangle
    elif len(approx) == 4:
        # compute the bounding box of the contour and use the
        # bounding box to compute the aspect ratio
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)

        # a square will have an aspect ratio that is approximately
        # equal to one, otherwise, the shape is a rectangle
        shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"

    # if the shape is a pentagon, it will have 5 vertices
    elif len(approx) == 5:
        shape = "pentagon"

    # otherwise, we assume the shape is a circle
    else:
        shape = "circle"

    # return the name of the shape
    return shape


while(cap.isOpened):
    # start taking image from webcam
    _, image = cap.read()

    # edge detection using canny methode
    canny = cv2.Canny(image, 80, 240, 3)

    # find contours in the  image and initialize the
    # shape detector
    cnts, hierarchy = cv2.findContours(
        canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # list
    shapes = []
    shapesSgtg = []
    results = []

    # detecting shape square and triangle, and save the index number
    for cIdx, c in enumerate(cnts):
        shape = detectshape(c)
        if shape == "square":
            shapes.append(cIdx)
        if shape == "triangle":
            shapesSgtg.append(cIdx)

    # checking, is the triangle a child of square
    for x in shapesSgtg:
        for y in shapes:
            if hierarchy[0][x][3] == y:
                results.append(x)

    # marking the detection in the image and labelling
    for result in results:
        counts = cnts[result]
        M = cv2.moments(counts)
        cX = int((M["m10"] / M["m00"]))
        cY = int((M["m01"] / M["m00"]))
        counts = counts.astype("float")
        counts = counts.astype("int")
        cv2.drawContours(image, [counts], -1, (0, 255, 0), 2)
        cv2.putText(image, "Segitiga dalam kotak", (cX, cY),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # show the result
    cv2.imshow("Image", image)
    cv2.imshow("tres", canny)
    if cv2.waitKey(10) & 0xFF == 27:
        cap.release()
        cv2.destroyAllWindows()
        break
