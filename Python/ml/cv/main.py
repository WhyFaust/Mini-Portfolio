import tensorflow as tf
import numpy as np
from PIL import Image
import requests
import tensorflow_hub as hub


# Загрузка предобученной модели из TensorFlow Hub
MODEL_URL = "https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet1k_s/classification/2"
model = hub.load(MODEL_URL)


def load_and_preprocess_image(img_path):
    """
    Функция для загрузки и предобработки изображения
    перед передачей в модель.
    """
    img = Image.open(img_path)  # Открываем изображение
    img = img.resize((224, 224))  # Изменяем размер до 224x224 пикселя
    img_array = np.array(img) / 255.0  # Нормализация значений (0-1)
    img_array = np.expand_dims(img_array, axis=0).astype(np.float32)  # Добавляем batch-дименсию
    return img_array


# Загрузка и предобработка изображения
image_path = "img1.jpg"  # Путь к изображению
image = load_and_preprocess_image(image_path)


# Получение предсказаний модели
preds = model(image)


# Преобразование предсказаний в вероятности
probabilities = tf.nn.softmax(preds, axis=-1)[0]


# Получение меток классов
LABELS_URL = "https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt"
labels = requests.get(LABELS_URL).text.splitlines()


# Определение наиболее вероятного класса
probable_index = np.argmax(probabilities)
print(f'На изображении: {labels[probable_index]} ({probabilities[probable_index] * 100:.2f}%)')


# Получение топ-5 предсказаний
top_5_indices = np.argsort(probabilities)[::-1][:5]
print("Топ-5 предсказаний:")
for i in top_5_indices:
    print(f'{labels[i]}: {probabilities[i] * 100:.2f}%')


# Проверка принадлежности объекта к конкретному классу (например, "banana")
object_name = "banana"
if object_name in labels:
    banana_index = labels.index(object_name)
    print(f'Вероятность, что на изображении {object_name}: {probabilities[banana_index] * 100:.2f}%')
else:
    print(f'Класс "{object_name}" не найден в загруженных метках.')