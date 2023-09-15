import os
import time
from transformers import AutoFeatureExtractor, AutoModelForImageClassification
import torch
from PIL import Image
from sklearn.metrics import accuracy_score


extractor = AutoFeatureExtractor.from_pretrained("weights/my_model")
vit_model = AutoModelForImageClassification.from_pretrained("weights/my_model")


def model_use(model, img):
    with torch.no_grad():
        logits = model(**img).logits

    predicted_label = logits.argmax(-1).item()

    return model.config.id2label[predicted_label]


path = "data/"
images_list = os.listdir(path)


def size_measurement(model):
    param_size = 0
    for param in model.parameters():
        param_size += param.nelement() * param.element_size()

    buffer_size = 0
    for buffer in model.buffers():
        buffer_size += buffer.nelement() * buffer.element_size()

    size_all_mb = (param_size + buffer_size) / (1024 ** 2)
    print('model size: {:.3f}MB'.format(size_all_mb))

size_measurement(vit_model)

# Квантизируем модель
quantized_model = torch.quantization.quantize_dynamic(vit_model, {torch.nn.Conv2d, torch.nn.Linear}, dtype=torch.qint8)

size_measurement(quantized_model)
start_time = time.time()

# Собака 1, кошка 0.
target_list = []
predict_list = []

for element in images_list:

    image = Image.open(path + element, mode='r', formats=None)

    inputs = extractor(image, return_tensors="pt")
    predict = model_use(quantized_model, inputs)
    target = element[:element.find(".")]

    if target == "dog":
        label = 1
    else:
        label = 0

    target_list.append(label)

    if predict == "dogs":
        pr = 1
    else:
        pr = 0

    predict_list.append(pr)

end_time = time.time()

acc = accuracy_score(target_list, predict_list)
print("Точность квантизированной модели= ", acc)
print("Время обработки изображений квантизированной модели= ", end_time-start_time, " секунд")
print("Скорость обработки изображений у квантизированной модели составила  ", len(images_list)/(end_time-start_time), " картинок в секунду")