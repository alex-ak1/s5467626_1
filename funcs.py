import os
import cv2
import matplotlib.pyplot as plt
import numpy as np


# Функция обработки изображения.
def processing_of_img(filename, choice_orientation, color_r, color_g, color_b, line_width):
    # Чтение изображения.
    img = cv2.imread(filename)

    # Определение расположения креста.
    choice_orientation = int(choice_orientation)

    # Определение корректных границ креста.
    if choice_orientation > 1 or choice_orientation < 0:
        choice_orientation = 0

    # Определение ширины линии.
    line_width = int(line_width)

    # Определение границ ширины линии.
    if line_width > 50 or line_width < 0:
        line_width = 10

    # Высота изображения.
    height = img.shape[0]
    # Ширина изображения.
    width = img.shape[1]

    # Копирование исходного изображения в нового.
    img_new = img

    # Цвет из составляющих в формате BGR.
    line_color = (int(color_b), int(color_g), int(color_r))
    # Рисование креста.
    if choice_orientation == 0:
        cv2.line(img_new, (width // 2, 0), (width // 2, height), line_color, line_width)
        cv2.line(img_new, (0, height // 2), (width, height // 2), line_color, line_width)
    else:
        cv2.line(img_new, (0, 0), (width, height), line_color, line_width)
        cv2.line(img_new, (width, 0), (0, height), line_color, line_width)

    # Разбиение имени файла.
    filename, file_extension = os.path.splitext(filename)
    filename_new = filename + '_new' + file_extension

    # Сохранение нового изображения.
    cv2.imwrite(filename_new, img_new)

    return filename_new


# Функция для построения графика распределения цветов.
def to_create_plot(filename):
    # Чтение изображения.
    img = cv2.imread(filename, cv2.IMREAD_COLOR)

    # Разбиение имени файла.
    filename, file_extension = os.path.splitext(filename)
    filename_plot = filename + '_plot' + file_extension

    img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    y, x, z = img_lab.shape
    flat_lab = np.reshape(img_lab, [y * x, z])

    colors = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    colors = np.reshape(colors, [y * x, z]) / 255.

    # Построение графика распределения цветов.
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs=flat_lab[:, 2], ys=flat_lab[:, 1], zs=flat_lab[:, 0], s=10, c=colors, lw=0)
    # Установка осей.
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Сохранение графика в файл.
    fig.savefig(filename_plot)

    return filename_plot
