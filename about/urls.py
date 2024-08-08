from django.urls import path
from . import views

# app_name = "about" WHY ???????? Blocks the fking redirects !!
urlpatterns = [
    path("about/", views.about, name="about"),
    path("", views.about, name="about"),
]
