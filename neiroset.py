import streamlit as st
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing import image

# Загрузите предварительно обученную модель h5 https://github.com/LinkInWorld/bird_recognition/releases
# !wget -O model.h5 "https://drive.google.com/uc?export=download&id=1Iur8carY3Izn7CxPdYGHOOA5DiN0Gj2v"
# model= keras.models.load_model('model.h5', custom_objects={'F1_score':'F1_score'})
model = keras.models.load_model('./releases/model.h5', custom_objects={'F1_score':'F1_score'})
# class_labels =


# Создайте Streamlit веб-приложение
st.title('Определение вида птицы')

# Добавьте загрузку изображения через браузер
uploaded_image = st.file_uploader("Загрузите изображение птицы", type=["jpg", "png", "jpeg"])


if uploaded_image is not None:
  st.image(uploaded_image, caption='Загруженное изображение', use_column_width=True)
  st.write(f'Предсказанный класс: Гусь')

if uploaded_image is not None:
    img = image.load_img(uploaded_image, target_size=(224, 224), grayscale=False)
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0, axis=0)

    # Выполните классификацию изображения
    predictions = model.predict(img)
    predicted_class = np.argmax(predictions)
    predicted_label = class_labels[predicted_class]
  
    # Выведите результат
    st.image(uploaded_image, caption='Загруженное изображение', use_column_width=True)
    st.write(f'Предсказанный класс: {predicted_label}')
