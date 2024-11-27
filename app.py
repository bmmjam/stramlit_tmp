import streamlit as st
import pandas as pd
import os
import csv

students_data = [
    {"ID": "001", "Base": 120},
    {"ID": "060", "Base": 60},
    {"ID": "055", "Base": 50},
    {"ID": "006", "Base": 40},
    {"ID": "031", "Base": 40},
    {"ID": "073", "Base": 40},
    {"ID": "021", "Base": 30},
    {"ID": "056", "Base": 30},
    {"ID": "061", "Base": 30},
    {"ID": "051", "Base": 20},
]


# Функция для генерации числового диапазона
def calculate_ranges(base, coefficient):
    start = (coefficient - 1) * base + 1
    end = coefficient * base
    return f"{start}-{end}"


st.title("Лабы деда комплингвистика")
st.info("В боковой панели введите выбранный коэффициент")
st.header("Визуальное представление своего варианта")

coefficient = st.slider("Выберите шаг для конкретных N слов", min_value=1, max_value=27, value=1)

# Вычисление значений для таблицы
data = []
for student in students_data:
    id = student["ID"]
    base = student["Base"]
    range_str = calculate_ranges(base, coefficient)
    data.append({"ID": id, "Base Range": f"1-{base}", "Adjusted Range": range_str})

df_task = pd.DataFrame(data)
st.table(df_task)


# Получаем директорию, где находится скрипт app.py
script_dir = os.path.dirname(os.path.abspath(__file__))
upload_folder = os.path.join(script_dir, "uploaded_files")

# Выводим текущую рабочую директорию и путь сохранения файлов
st.write(f"Текущая рабочая директория: {os.getcwd()}")
st.write(f"Файлы будут сохранены в: {upload_folder}")

# Создание папки для сохранения файлов, если ее нет
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)

# Загрузка файлов от студентов
st.write("### Загрузите свой файл")
uploaded_file = st.file_uploader("Выберите файл для загрузки", type=["txt"])

if uploaded_file is not None:
    # Сохранение файла на сервере
    save_path = os.path.join(upload_folder, uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Файл {uploaded_file.name} успешно загружен и сохранен на сервере.")
    st.write(f"Файл сохранен по пути: {save_path}")


