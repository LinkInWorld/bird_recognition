import streamlit as st
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import numpy as np

# Загрузите предварительно обученную модель h5
#model_path = 'https://disk.yandex.lt/d/6C6Dk6tiIMZAbw'
#model = keras.models.load_model(model_path)

# Загрузите файл с метками классов
#class_labels_path = 'путь_к_файлу/class_labels.txt'
#with open(class_labels_path, 'r') as file:
#    class_labels = [line.strip() for line in file.readlines()]

# Создайте Streamlit веб-приложение
st.title('Определение вида птицы')

# Добавьте загрузку изображения через браузер
uploaded_image = st.file_uploader("Загрузите изображение птицы", type=["jpg", "png", "jpeg"])
***
if uploaded_image is not None:
    img = image.load_img(uploaded_image, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)

    # Выполните классификацию изображения
    predictions = model.predict(img)
    predicted_class = np.argmax(predictions)
    predicted_label = class_labels[predicted_class]
***

    # Выведите результат
    st.image(uploaded_image, caption='Загруженное изображение', use_column_width=True)
    st.write(f'Предсказанный класс: {predicted_label}')
