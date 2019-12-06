import cv2
from imutils import paths


images = r"D:\blink_data\closedeyes"

imagePaths = sorted(list(paths.list_images(images)))

n = 0

for imagePath in imagePaths:
    n += 1
    print(n)
    image = cv2.imread(imagePath)
    name_image = f'D:\\blink_data\\blink_mix\\close.{n}.jpg'
    cv2.imwrite(name_image, image)

