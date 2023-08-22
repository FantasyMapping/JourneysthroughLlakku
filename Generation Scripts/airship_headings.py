from PIL import Image
import cv2
from pathlib import Path
import numpy as np
airship_graphic=Path("RenderedRedFortune.png")
Original_Image = cv2.imread(airship_graphic.as_posix(),cv2.IMREAD_UNCHANGED)
print(Original_Image.shape)
def rotate_image(img, angle,size):
    size_reverse = np.array(img.shape[1::-1]) # swap x with y
    M = cv2.getRotationMatrix2D(tuple(size_reverse / 2.), angle, 1.)
    MM = np.absolute(M[:,:2])
    #size_new = MM @ size_reverse

    M[:,-1] += (size - size_reverse) / 2.
    return cv2.warpAffine(img, M, tuple(size))

#create new headings
headings=np.linspace(0,360,37)
for angle in headings:
    rotated_image1 = rotate_image(Original_Image,angle,size=[4000,4000])
    cv2.imwrite("Airship Assets/Airship Headings/RenderedRedFortune{:02d}deg.png".format(int(angle)),rotated_image1)