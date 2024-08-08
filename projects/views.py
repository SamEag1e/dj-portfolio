from django.shortcuts import render, get_object_or_404
from .models import Project, Tag


def projects(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    return render(
        request, "projects/projects.html", {"projects": projects, "tags": tags}
    )


def project_details(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(
        request, "projects/project_detail.html", {"project": project}
    )
