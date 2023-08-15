from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import FileField, RadioField
from wtforms.fields import html5 as h5fields
from wtforms.widgets import html5 as h5widgets


# Форма для загрузки изображения и выбора параметров.
class ImageForm(FlaskForm):
    choice_orientation = RadioField('Ориентация креста:',
                                    choices=[('0', 'горизонтальная'),
                                             ('1', 'вертикальная')], default='0')
    # Поле для красной составляющей креста (R).
    color_r_range = h5fields.IntegerRangeField('',
                                               widget=h5widgets.RangeInput(step=1),
                                               default=255)
    color_r = h5fields.IntegerRangeField('Красная составляющая (R):',
                                         widget=h5widgets.NumberInput(min=0, max=255, step=1),
                                         default=255)
    # Поле для зелёной составляющей креста (G).
    color_g_range = h5fields.IntegerRangeField('',
                                               widget=h5widgets.RangeInput(step=1),
                                               default=255)
    color_g = h5fields.IntegerRangeField('Зелёная составляющая (G):',
                                         widget=h5widgets.NumberInput(min=0, max=255, step=1),
                                         default=255)
    # Поле для синей составляющей креста (B).
    color_b_range = h5fields.IntegerRangeField('',
                                               widget=h5widgets.RangeInput(step=1),
                                               default=255)
    color_b = h5fields.IntegerRangeField('Синяя составляющая (B):',
                                         widget=h5widgets.NumberInput(min=0, max=255, step=1),
                                         default=255)
    # Толщина линии.
    line_width_range = h5fields.IntegerRangeField('',
                                                  widget=h5widgets.RangeInput(step=1),
                                                  default=10)
    line_width = h5fields.IntegerRangeField('Толщина линии (px):',
                                            widget=h5widgets.NumberInput(min=1, max=50, step=1),
                                            default=10)
    # Поле загрузки файла. Валидатор укажет ввести корректный файл.
    img = FileField('Выберите файл изображения:',
                    validators=[FileRequired(),
                                FileAllowed(['jpg', 'jpeg', 'png'],
                                            'Только файлы изображений!')])
