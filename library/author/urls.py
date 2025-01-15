from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.author_list, name='author_list'),
    path('add/', views.add_author, name='add_author'),
    path('delete/<int:author_id>/', views.delete_author, name='delete_author'),
]