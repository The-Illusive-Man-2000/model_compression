### ITMO_Model compression

$~~~~~~~~~$

__Описание файлов репозитория:__

***
vit_model_run.py $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ _Запуска трансформера ViT обученного для классификации кошек и собак на изображениях._

resnet.py $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ _Запуска ResNet, предварительно обученная на ImageNet-1k для cats/dogs, с разрешением 224x224._

requirements.txt  $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ _Список библиотек и их версий._

***
__Папка data__

$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$   _Папка для изображений кошек и собак (160 картинок, 80 кошек и 80 собак)._


***
__Папка weights/my_model__  $~~~~~~~~~~~~~~$  _Папка с весами и конфигурационными файлами трансформера._


***


Базовые замеры метрик производительности (скорости и точности) модели (на CPU).


| Сравнение                       | Accuracy            | Обработанных фото в сек | Количество секунд| Вес модели (мегабайт)|
| :-------------------------------|:-------------------:|:-----------------------:|:----------------:|:--------------------:|
| исходный ViT                    | 0.9875              | 0.1776                  | 900.8722         | 327.302              |
| конвертированный в ONNX ViT     | 0.9875              | 8.421                   | 19               | 327.552              |
| конвертированный в TensorRT ViT | 0.9875              | 23.767                  | 6.73             | 327.302              |
| конвертированный в OpenVINO     | 0.9875              | 7.9526                  | 20.11            | 163.65               |


***
Ссылка на данные, на которых делался замер и на веса модели.

- ViT: https://drive.google.com/drive/folders/1YN1uM3D5oRoX8wQ2GAX3juVuZlh3YxjJ?usp=sharing
- Resnet-50: https://drive.google.com/drive/folders/1XT7pq6VVNLiV0F-RS0iPdTYNwE0mS-OF?usp=sharing 
