import numpy as np
import cv2

def preprocess(img_data):
    mean_vec = np.array([0.485, 0.456, 0.406])[::-1]
    stddev_vec = np.array([0.229, 0.224, 0.225])[::-1]
    norm_img_data = np.zeros(img_data.shape).astype('float32')
    for i in range(img_data.shape[2]):
        norm_img_data[:,:,i] = (img_data[:,:,i]/255 - mean_vec[i]) / stddev_vec[i]

    return norm_img_data

if __name__ == '__main__':
    file_name = r'D:\code_python\Meduza\app-blink\train_model\image_test\new_color40.jpg'
    input_image: int = cv2.imread(file_name)
    if input_image is not None:
        ## 画像のリサイズ
        resized = cv2.resize(input_image, (28, 28))
        ## 画像のスケーリング/正規化
        preprocessed = preprocess(resized)
        ## Blob形式に変換(行列形状の変換)
        blob = cv2.dnn.blobFromImage(preprocessed)
        print(blob.shape)
        ## ONNXファイルの読み込み
        #model_file = 'resnet50/model.onnx'
        model_file = r'D:\code_python\Meduza\app-blink\train_model\model\net2_gay_test_TF.pb'
        # net = cv2.dnn.readNetFromONNX(model_file)
        net = cv2.dnn.readNet(model_file)
        ## 入力画像データの指定
        net.setInput(blob)
        # ## フォワードパス(順伝播)の計算 & 不要な次元の削除
        # pred = np.squeeze(net.forward())
        # print(pred.shape)
        # print(sum(pred))
        print(net.forward())
        # ImageNet(ILSVRC2012)のカテゴリ定義ファイルの読み込み
        # rows = open("synset.txt").read().strip().split("\n")
        # classes = [r[r.find(" ") + 1:].split(",")[0] for r in rows]
        # ## 推論結果から信頼度の高い順にソートして上位5件のカテゴリ出力
        # indexes = np.argsort(pred)[::-1][:5]
        # for i in indexes:
        #     text = "{}: {:.2f}%".format(classes[i], pred[i] * 100)
        #     print(text)
