from django.db import models

class Articles(models.Model):
    title = models.CharField('Назва', max_length=50, default='')
    anons = models.CharField('Анонс', max_length=250, default='')
    full_text = models.TextField('Стаття')
    date = models.DateTimeField('Дата публікації')

    def __str__(self):
        return f'Новина: {self.title}'

    class Meta:
        verbose_name = 'новина'
        verbose_name_plural = 'новини'