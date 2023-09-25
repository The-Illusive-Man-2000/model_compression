### ITMO_Model compression

$~~~~~~~~~$

__Quantization and Pruning:__


***


Замеры метрик производительности (скорости, точности и веса) модели (на CPU).


| Модель                                                    | Accuracy |    Обработанных фото в сек    | Количество секунд | Вес модели (мегабайт) |
|:----------------------------------------------------------|:--------:|:-----------------------------:|:-----------------:|:---------------------:|    
| базовый ViT                                               |  0.9875  |            0.1776             |     900.8722      |          327          |
| pretrained resnet-50                                      |  0.597   |       2.729779799241981       |      219.797      |          98           |
| ViT после квантизации (Dynamic Quantization)              |  0.975   |            2.6346             |      60.7292      |         2.979         |
| ViT после квантизации (Dynamic Quantization (Optimum))    |  0.9875  |            7.7269             |      20.7068      |         83.07         |
| ViT после квантизации (Post Training Static Quantization) |   0.5    |            12.3893            |      12.9143      |         0.727         |
| ViT после прунинга (local unstructured pruning)           |  0.975   |             1.818             |      87.9607      |        327.302        |
| ViT после прунинга (global unstructured pruning)          |   0.95   |            0.1819             |        879        |        329.561        |
| ViT после прунинга (multiple param. structured pruning)   | 0.95625  |            8.4135             |       19.01       |        327.302        |



***
Ссылка на данные, на которых делался замер и на веса модели.

- ViT: https://drive.google.com/drive/folders/1YN1uM3D5oRoX8wQ2GAX3juVuZlh3YxjJ?usp=sharing
- Resnet-50: https://drive.google.com/drive/folders/1XT7pq6VVNLiV0F-RS0iPdTYNwE0mS-OF?usp=sharing 
