### ITMO_Model compression

$~~~~~~~~~$

__Описание файлов репозитория:__

vit_model_run.py $~~~~~~~~~$ _Запуска трансформера ViT обученного для классификации кошек и собак на изображениях._

requirements.txt  $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ _Список библиотек и их версий._

***
__Папка data__

$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$   _Папка для изображений кошек и собак (600 картинко, 300 кошек и 300 собак)._


***
__Папка weights/my_model__  $~~~~~~$  _Папка с весами и конфигурационными файлами трансформера._


***


Базовые замеры метрик производительности (скорости и точности) модели (на CPU).

Сравнение                    | Detecto              |   
:----------------------------|:--------------------:|
Accuracy                     | 0.9966666666666667   | 
Обработанных фото в секунду  | 6.44                 | 
Количество секунд            | 93.157               |
Вес модели (мегабайт)        | 327                  |
