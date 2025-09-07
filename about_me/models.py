from django.db import models


class Person(models.Model):
  first_name = models.CharField(max_length=50, verbose_name='Имя')
  last_name = models.CharField(max_length=50, verbose_name='Фамилия')
  age = models.SmallIntegerField(default=18, verbose_name='Возраст')
  email = models.EmailField(verbose_name='Почта')
  image = models.ImageField(upload_to='profile_pics/', verbose_name='Фото профиля')
  