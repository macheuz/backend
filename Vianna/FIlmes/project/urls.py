
from django.contrib import admin
from django.urls import path
from app.views import home, filmes, create, view, edit, update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('filmes/', filmes, name='filmes'),
    path('create/', create, name='create'),
    path('view/<int:pk>', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
]
