import cv2
import tensorflow as tf
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras import backend as K
from lenet import LeNet


name_model = "net_inference.h5"


#
#
# def covert_to_cnn(name_model):
# 	name = name_model[:-3]
# 	PATH_MODEL = r"model/" + name_model
# 	net = load_model(PATH_MODEL)
#
#     in_model = LeNet.build_2_new_inference(width=28, height=28, depth=2, classes=2)
#
# 	in_model.load_weights(f"{name_model}_weight.h5")
#
# 	opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
# 	in_model.compile(loss="binary_crossentropy", optimizer=opt,metrics=["accuracy"])
#
# 	sess = K.get_session()
# 	outname = "output_node"
#
# 	tf.identity(net.outputs[0], name=outname)
# 	constant_graph = tf.graph_util.convert_variables_to_constants(sess, sess.graph.as_graph_def(), [outname])
# 	tf.io.write_graph(constant_graph, r"model", f"{name}_TF.pb", as_text=False)
#
# 	net_cv = cv2.dnn.readNet(r"model/"+ name + "_TF.pb")
#
# 	in_model.load_weights(f"{name_model}_weight.h5")
#
#
#
# 	print("The Model Works in Opencv ")


def preprocess(img_data):
    mean_vec = np.array([0.485, 0.456, 0.406])[::-1]
    stddev_vec = np.array([0.229, 0.224, 0.225])[::-1]
    norm_img_data = np.zeros(img_data.shape).astype('float32')
    for i in range(img_data.shape[2]):
        norm_img_data[:,:,i] = (img_data[:,:,i]/255 - mean_vec[i]) / stddev_vec[i]

    return norm_img_data



def test_net(model, image):

	i = cv2.imread(image)

	brightYCB = cv2.cvtColor(i, cv2.COLOR_BGR2YCrCb)
	im = cv2.cvtColor(brightYCB, cv2.COLOR_BGR2GRAY)
	net = cv2.dnn.readNet(model)
	blob = cv2.dnn.blobFromImage(im, size=(28, 28), swapRB=True)
	net.setInput(blob)
	return net.forward()

if __name__ == '__main__':
	
	image =  r"D:\code_python\Meduza\app-blink\train_model\data\open_eye.jpg"
	path_image = r"D:\code_python\Meduza\app-blink\train_model\image_test"
	model = r"D:\code_python\Meduza\app-blink\train_model\model\net2_gay_test_new_TF.pb"

	for i in range(120):
		img = r'\new_color{}.jpg'.format(i+1)
		im = path_image + img
		#
		status = test_net(model, im)[-1]
		print(status)

