import cv2
from cv2 import dnn_superres
def run(input_path):
    img = cv2.imread(input_path)  # 读取720p的图像
    trained_model_path = 'models/ESPCN_x3.pb'  # 训练好的ESPCN_x2模型的存储路径

    sr = dnn_superres.DnnSuperResImpl_create()  # 实例化对象
    sr.readModel(trained_model_path)  # 读取ESPCN_x2模型
    sr.setModel('espcn', 3)  # 设置超分图像放大比例（与训练模型的超分倍数一致），放大图像
    result = sr.upsample(img)  # 上采样，超分
    return result