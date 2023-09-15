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


| Сравнение                  | предобученный ViT  | pretrained resnet-50 |
| :-------------------------|:-------------------:|:--------------------:|
| Accuracy                  | 0.9875              | 0.597                |
| Обработанных фото в сек   | 0.1776              | 2.729779799241981    |
| Количество секунд         | 900.8722            | 219.797              |
| Вес модели (мегабайт)     | 327                 | 98                   |

***
Ссылка на данные, на которых делался замер и на веса модели.

- ViT: https://drive.google.com/drive/folders/1YN1uM3D5oRoX8wQ2GAX3juVuZlh3YxjJ?usp=sharing
- Resnet-50: https://drive.google.com/drive/folders/1XT7pq6VVNLiV0F-RS0iPdTYNwE0mS-OF?usp=sharing 
