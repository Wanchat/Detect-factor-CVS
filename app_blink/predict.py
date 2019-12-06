import cv2
# from keras.models import load_model
# from tensorflow.python.keras.models import load_model
# from tensorflow.python.keras.preprocessing.image import img_to_array
# from keras_preprocessing.image import img_to_array
import numpy as np

def pre_process(window_eye):
    window = cv2.resize(window_eye, (28, 28))
    window = window.astype("float") / 255.0
    window = img_to_array(window)
    window = np.expand_dims(window, axis=0)
    return window

def dnn_predict(model, image):
    net =cv2.dnn.readNet(model)
    net.setInput(cv2.dnn.blobFromImage(image, size=(28, 28),swapRB=True,crop=False))
    return net.forward()

p = "lowcast/model/inference_net2_TF.pb"

net =cv2.dnn.readNet(p)


# path_model_keras = r"D:\code_python\app_blink\train_model\model\net2_gay_test_TF.h5")

# m = load_model(path_model_keras)

# for i in range(100):
#     p = f"D:\\code_python\\app_blink\\train_model\\image_test\\new_color{i+1}.jpg"
#     im = cv2.imread(p)
#     gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)

#     im_p = pre_process(gray)

#     score = m.predict(im_p)[-1]

#     if score[0]> score[1]:
#         label = "closed"
#     else:
#         label = "opened"

#     print(f"{label} {score}")
