import streamlit as st

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import numpy as np

# Загрузите предварительно обученную модель h5
model_path = 'путь_к_файлу/model.h5'
model = keras.models.load_model(model_path)

# Загрузите изображение, которое вы хотите классифицировать
img = st.file_uploader("Pick a file")
#img = 'путь_к_изображению/птица.jpg'
#img = image.load_img(image_path, target_size=(224, 224))  # Предположим, что модель требует изображения размером 224x224 пикселя
img = image.img_to_array(img)
img = np.expand_dims(img, axis=0)

# Выполните классификацию изображения
predictions = model.predict(img)

# Предположим, что модель возвращает вероятности классов
# Найдите индекс класса с максимальной вероятностью
predicted_class = np.argmax(predictions)

# Загрузите файл с метками классов, чтобы узнать, какой класс соответствует предсказанию
class_labels_path = 'путь_к_файлу/class_labels.txt'
with open(class_labels_path, 'r') as file:
    class_labels = [line.strip() for line in file.readlines()]

# Определите название предсказанного класса
predicted_label = class_labels[predicted_class]

# Выведите результат

st.write('Предсказанный класс:', predicted_label)
#print(f'Предсказанный класс: {predicted_label}')
