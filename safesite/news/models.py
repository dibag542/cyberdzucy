from django.db import models

class Articles(models.Model):

    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
