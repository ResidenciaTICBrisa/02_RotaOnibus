# Django Rest Framework

## Requisitos

```python
python3 -m venv venv
pip install django
pip install djangorestframework
```

## Começando o projeto

Precisamos startar o projeto e criar o app.

```python
django-admin startproject library .
django-admin startapp books
```

### INSTALLED_APPS

- Adicionar 'books' e 'rest_framework' em INSTALLED_APPS.
- Criar página api dentro de books (padrão de projeto).

### Adicionando o modelo da entidade

- books/models.py

```python
from django.db import models
from uuid import uuid4

class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
```

### Serializando

- books/serializers.py

```python
from rest_framework import serializers
from books import models

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Books
        fields = '__all__'
```

### Viewsets

- books/viewsets.py

```python
from rest_framework import viewsets
from books.api import serializers
from books import models

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BooksSerializer
    queryset = models.Books.objects.all()
```

### Adicionando a rota da API

- library/urls.py

```python
from django.contrib import admin
from django.urls import path, include

from books.api import viewsets as booksviewsets

from rest_framework import routers

route = routers.DefaultRouter()
route.register(r'books', booksviewsets.BooksViewSet, basename='Books')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
```

## Fazendo migrações

```python
python manage.py makemigrations
python manage.py migrate
```
## Rodando o projeto

```python
python manage.py runserver
```
Agora você pode acessar o frontend disponibilizado pelo próprio Django ou fazer requisiões diretamente pela URL.