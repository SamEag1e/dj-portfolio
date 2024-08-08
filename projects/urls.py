from django.urls import path
from . import views

# app_name = "projects"  # WHY THIS DOESN'T WORK ???
urlpatterns = [
    path("", views.projects, name="projects"),
    path("<int:pk>", views.project_details, name="project_details"),
]
