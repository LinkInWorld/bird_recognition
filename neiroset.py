import streamlit as st
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing import image

# model= keras.models.load_model('./model.h5', custom_objects={'F1_score':'F1_score'})

# Создайте Streamlit веб-приложение
st.title('Определение вида птицы')

# Добавьте загрузку изображения через браузер
uploaded_image = st.file_uploader("Загрузите изображение птицы", type=["jpg", "png", "jpeg"])


if uploaded_image is not None:  
    # Выведите результат
    st.image(uploaded_image, caption='Загруженное изображение', use_column_width=True)
    st.write(f'Предсказанный класс: {predicted_label}')
