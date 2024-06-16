import cv2

def extract_symbols(img_path):
    img = cv2.imread(img_path, 0)

    # Применяем GaussianBlur для сглаживания изображения
    blurred = cv2.GaussianBlur(img, (5, 5), 0)

    # Применяем threshold для бинаризации изображения
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

    # Ищем контуры символов на бинаризованном изображении
    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Сортируем контуры слева направо
    contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])

    # Создаем пустой список для сохранения символов
    chars = []

    for contour in contours:
        # Получаем координаты ограничивающего прямоугольника контура
        (x, y, w, h) = cv2.boundingRect(contour)

        # Ограничиваем каждый символ ограничивающим прямоугольником
        char_img = thresh[y:y + h, x:x + w]

        # Устанавливаем размеры для нормализованных символов
        resized_char_img = cv2.resize(char_img, (150, 150))

        # Добавляем символ в список
        chars.append(resized_char_img)

    # Возвращаем список нормализованных символов
    return chars


import os
import cv2
import numpy as np
from keras.models import load_model

# Загружаем модель нейросети
model = load_model('weights.h5')

# Загружаем изображение номера машины
img_path = 'NumBaseCrop\\7.bmp'
img = cv2.imread(img_path)

# Извлекаем отдельные символы номера машины на изображении
# Здесь можно использовать методы для поиска символов, такие как 
# cv2.findContours или cv2.connectedComponents для нахождения группы близлежащих пикселей
# затем можно вырезать символы и пропустить их через нейросеть для распознавания.
symbols = extract_symbols(img_path) 

# Склеиваем распознанные символы в одну строку
car_number = ''
for symbol in symbols:
    # Предобработка изображения символа для подготовки к распознаванию
    processed_symbol = symbol.reshape(1, 150, 150, 1)
    processed_symbol = processed_symbol / 255

    # Получение распознанного символа от нейросети
    predicted = model.predict(processed_symbol)
    car_number += labels[np.argmax(predicted)]

print('Номер машины: ', car_number)
