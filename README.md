### ITMO_Model compression

$~~~~~~~~~$

__Quantization and Pruning:__


***


Базовые замеры метрик производительности (скорости и точности) модели (на CPU).


| Сравнение                  | предобученный ViT  | pretrained resnet-50 |
| :-------------------------|:-------------------:|:-------------------:|
| Accuracy                  | 0.9966666666666667  | 0.597                 |
| Обработанных фото в сек   | 6.44                | 2.729779799241981                   |
| Количество секунд         | 93.157              | 219.797                   |
| Вес модели (мегабайт)     | 327                 | 98                   |

***
Ссылка на данные, на которых делался замер и на веса модели.

- ViT: https://drive.google.com/drive/folders/1YN1uM3D5oRoX8wQ2GAX3juVuZlh3YxjJ?usp=sharing
- Resnet-50: https://drive.google.com/drive/folders/1XT7pq6VVNLiV0F-RS0iPdTYNwE0mS-OF?usp=sharing 
