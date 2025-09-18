from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
        path('create/', views.create_view, name='create_view'),
    path('list/', views.list_view, name='list_view'),
    path('update/<int:pk>/', views.update_view, name='update_view'),
    path('delete/<int:pk>/', views.delete_view, name='delete_view'),
]
