import os
import time
from transformers import AutoImageProcessor, ResNetForImageClassification
import torch
from PIL import Image
from sklearn.metrics import accuracy_score

start_time = time.time()

extractor = AutoImageProcessor.from_pretrained("weights/my_resnet-50")
model = ResNetForImageClassification.from_pretrained("weights/my_resnet-50")

def model_infer(model, img):
    with torch.no_grad():
        logits = model(**img).logits

    predicted_label = logits.argmax(-1).item()

    return model.config.id2label[predicted_label]

path = "data/"
images_list = os.listdir(path)

# dog 1, cat 0.
target_list = []
predict_list = []

for element in images_list:

    image = Image.open(os.path.join(path, element), mode='r')

    inputs = extractor(image, return_tensors="pt")
    predict = model_infer(model, inputs)
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

model.save_pretrained("saved_resnet_model")

end_time = time.time()

accuracy = accuracy_score(target_list, predict_list)
print("Точность = ", accuracy)
print("Время обработки изображений = ", end_time - start_time, " секунд")
print("Скорость обработки изображений составила  ", len(images_list) / (end_time - start_time), " картинок в секунду")
