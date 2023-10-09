from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default='News_name')
    anons = models.CharField('Анонс', max_length=250, default='anons')
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return f'Новость: {self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
