import os

from flask import Flask
from flask import render_template
from werkzeug.utils import secure_filename

from ImageForm import ImageForm
from funcs import processing_of_img, to_create_plot

app = Flask(__name__)

# Используем CSRF-токен.
SECRET_KEY = 'secret'
app.config['SECRET_KEY'] = SECRET_KEY


# Декоратор для вывода страницы по умолчанию (главной страницы).
@app.route("/")
def index():
    # Передаем данные в шаблон и вызываем его.
    return render_template('index.html')


# Декоратор для вывода страницы загрузки изображения.
@app.route('/run', methods=['GET', 'POST'])
def run_app():
    # Форма.
    form = ImageForm()
    if form.validate_on_submit():
        # Получаем имя файла-изображения.
        filename_img = os.path.join(r'./static/images',
                                    secure_filename(form.img.data.filename))

        # Сохраняем файл-изображение на сервере.
        form.img.data.save(filename_img)
        # Производим обработку изображения по указанным опциям.
        filename_img_new = processing_of_img(filename_img, form.choice_orientation.data,
                                             form.color_r.data, form.color_g.data, form.color_b.data,
                                             form.line_width.data)
        # Создаём график распределения цветов для исходного изображения (1).
        filename_img_plot = to_create_plot(filename_img)
        # Создаём график распределения цветов для полученного изображения.
        filename_img_new_plot = to_create_plot(filename_img_new)

        # Передаём переменные в шаблон.
        return render_template('result.html',
                               img=filename_img,
                               img_new=filename_img_new,
                               img_plot=filename_img_plot,
                               img_new_plot=filename_img_new_plot,
                               )
    else:
        return render_template('form.html', form=form, result=u'Загрузите файл-изображение!')


# Запуск.
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=False)
