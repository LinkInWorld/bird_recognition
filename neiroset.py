import streamlit as st

# Создайте Streamlit веб-приложение
st.title('Определение вида птицы')

# Добавьте загрузку изображения через браузер
uploaded_image = st.file_uploader("Загрузите изображение птицы", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
  st.image(uploaded_image, caption='Загруженное изображение', use_column_width=True)
  st.write(f'Предсказанный класс: Гусь')
