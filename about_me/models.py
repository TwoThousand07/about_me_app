from django.db import models

from django.utils.translation import gettext_lazy as _

class Person(models.Model):
  first_name = models.CharField(max_length=50, verbose_name=_('Name'))
  last_name = models.CharField(max_length=50, verbose_name=_('Surname'))
  age = models.SmallIntegerField(default=18, verbose_name=_('Age'))
  email = models.EmailField(verbose_name= _('Email'))
  image = models.ImageField(upload_to='profile_pics/', verbose_name=_('Photo picture'), default='default_profile.png')

  def __str__(self):
    return f'{self.first_name} {self.last_name}'