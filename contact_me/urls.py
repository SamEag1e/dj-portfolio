from django.urls import path
from . import views

urlpatterns = [
    path("", views.contact_me, name="contact_me"),
    path("contact_success", views.contact_success, name="contact_success"),
]
