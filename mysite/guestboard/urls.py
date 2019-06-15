from django.urls import path
from guestboard import views

app_name = "guestboard"


urlpatterns = [
    path("", views.index_, name="index"),
    path("create/", views.create, name="create"),
]
