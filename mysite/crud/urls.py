from django.urls import path
from crud import views


app_name = "crud"

urlpatterns = [
    path(r'', views.list_, name='list'),
    path('create/', views.create, name='create'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete_, name='delete'),
]
