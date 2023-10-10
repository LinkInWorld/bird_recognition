import streamlit as st
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input

# Загрузите предварительно обученную модель h5 https://github.com/LinkInWorld/bird_recognition/releases

# Создайте Streamlit веб-приложение
st.title('Определение вида птицы')

# Добавьте загрузку изображения через браузер
uploaded_image = st.file_uploader("Загрузите изображение птицы", type=["jpg", "png", "jpeg"])


if uploaded_image is not None:
  st.image(uploaded_image, caption='Загруженное изображение', use_column_width=True)
  st.write(f'Предсказанный класс: Гусь')
