from django.urls import path
from guestboard import views

app_name = "guestboard"


urlpatterns = [
    path("", views.index, name="index"),
]
