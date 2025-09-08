from django.shortcuts import render

from .models import Person

def homepageview(request):
  person = Person.objects.get(first_name='Erzhan')
  return render(request, 'index.html', {'person': person})
