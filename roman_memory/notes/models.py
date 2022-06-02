from django.db import models
from datetime import datetime

# Таблица с текстовыми записями
class Notes(models.Model):
    title = models.CharField('Название', max_length=80)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Запись')
    date = models.DateTimeField('Дата записи', auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/notes'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

# image = models.FileField(upload_to='img/')