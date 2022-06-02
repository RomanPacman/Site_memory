from django.db import models


class Links(models.Model):
    title = models.CharField('Название', max_length=80)
    image = models.FileField('Превью', upload_to='links/img/')
    link = models.CharField('Ссылка', max_length=180)
    text = models.TextField('Описание')
    date = models.DateTimeField('Дата записи', auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/links/'

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
