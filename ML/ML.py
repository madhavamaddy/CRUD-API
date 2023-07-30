#use 3 python lib
import cv2
import numpy as np
import matplotlib.pyplot as plt


img=cv2.imread("IELTS-template.jpg")

#bgr to rgb
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#matplo method
plt.imshow(RGB_img)

# gui window
plt.waitforbuttonpress()
plt.close('all')
