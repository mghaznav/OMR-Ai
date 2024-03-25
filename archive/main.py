from imutils.perspective import four_point_transform
import argparse
import cv2 as cv
import numpy as np
import sys
import os

# Helper methods
def saveImgMod(nameMod, path, image):
    file_path, file_name = os.path.split(path)
    base, ext = os.path.splitext(file_name)
    new_file_name = f"{base}_{nameMod}{ext}"
    new_image_path = os.path.join(file_path, new_file_name)

    cv.imwrite(new_image_path, image)

# Parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image', type=str, required=True, help="Path to the buuble sheet image file")

args = parser.parse_args()

#TODO: Verify image format is supported from opencv documentation: https://docs.opencv.org/4.9.0/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56
image = cv.imread(args.image)

if image is None:
    print(f"Error: Failed to open {args.image}")
    sys.exit(1)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray, (5, 5), 0)
edged = cv.Canny(blurred, 75, 200)

kernel = np.ones((5,5), np.uint8)
dilated = cv.dilate(edged, kernel, iterations=1)
eroded = cv.erode(dilated, kernel, iterations=1)

# saveImgMod("blurred", args.image, blurred)
# saveImgMod("edged", args.image, edged)
# saveImgMod("eroded", args.image, eroded)

# find the bubblesheet
contours, _ = cv.findContours(eroded.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key = cv.contourArea, reverse = True)

bubbleSheet = None

for c in contours:
    peri = cv.arcLength(c, True)
    approx = cv.approxPolyDP(c, 0.02 * peri, True)

    if len(approx) == 4:
        bubbleSheet = approx
        break

# Draw the contour on the image and save it
cv.drawContours(image, [bubbleSheet], -1, (0, 255, 0), 2)
saveImgMod("sheet", args.image, image)

# Transform the image
paper = four_point_transform(image, bubbleSheet.reshape(4, 2))
warped = four_point_transform(gray, bubbleSheet.reshape(4, 2))
saveImgMod("transformed", args.image, paper)