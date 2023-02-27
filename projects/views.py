from django.shortcuts import render
from projects.models import Project

# Create your views here.

"""
General view for list of projects
"""
def project_index(request):

    projects = Project.objects.all()

    context = {

        'projects': projects

    }

    return render(request, 'project_index.html', context)

"""
Specific view for project details
"""
def project_detail(request, pk):

    project = Project.objects.get(pk=pk)

    context = {

        'project': project

    }

    return render(request, 'project_detail.html', context)