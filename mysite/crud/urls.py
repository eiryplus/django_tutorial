from django.urls import path
from crud import views


app_name = "crud"

urlpatterns = [
    path(r'', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
    path('edit/<int:editing_id>/', views.edit, name='edit'),
]
