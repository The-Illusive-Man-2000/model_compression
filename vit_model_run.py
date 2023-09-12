import os
import time
from transformers import AutoFeatureExtractor, AutoModelForImageClassification
import torch
from PIL import Image
from sklearn.metrics import accuracy_score


start_time = time.time()

extractor = AutoFeatureExtractor.from_pretrained("weights/my_model")
vit_model = AutoModelForImageClassification.from_pretrained("weights/my_model")


def model_use(model, img):
    with torch.no_grad():
        logits = model(**img).logits

    predicted_label = logits.argmax(-1).item()

    return model.config.id2label[predicted_label]


path = "data/"
images_list = os.listdir(path)

# Собака 1, кошка 0.
target_list = []
predict_list = []

for element in images_list:

    image = Image.open(path + element, mode='r', formats=None)

    inputs = extractor(image, return_tensors="pt")
    predict = model_use(vit_model, inputs)
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
print("Точность = ", acc)
print("Время обработки изображений = ", end_time-start_time, " секунд")
print("Скорость обработки изображений составила  ", len(images_list)/(end_time-start_time), " картинок в секунду")
