### ITMO_Model compression

$~~~~~~~~~$

__Quantization and Pruning:__


***


Замеры метрик производительности (скорости, точности и веса) модели (на CPU).


| Модель                    | Accuracy            | Обработанных фото в сек | Количество секунд | Вес модели (мегабайт) |
| :-------------------------|:-------------------:|:-----------------------:|:-----------------:|:---------------------:|    
| базовый ViT               | 0.9966666666666667  | 6.44                    | 93.157            | 327                   |
| pretrained resnet-50      | 0.597               | 2.729779799241981       | 219.797           | 98                    |
| ViT после квантизации     |                     |                         |                   |                       |
| ViT после прунинга        |                     |                         |                   |                       |



***
Ссылка на данные, на которых делался замер и на веса модели.

- ViT: https://drive.google.com/drive/folders/1YN1uM3D5oRoX8wQ2GAX3juVuZlh3YxjJ?usp=sharing
- Resnet-50: https://drive.google.com/drive/folders/1XT7pq6VVNLiV0F-RS0iPdTYNwE0mS-OF?usp=sharing 
