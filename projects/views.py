from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required  # this decorator used to block any view we want 



# Create your views here.

def projects(request):
    # msg = "here is the projects folder name"
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project': projectObj})

#  creating a view for our form
@login_required(login_url='login')
def createProject(request):
    form = ProjectForm()

# Check if the form is post and valid and save it in the database
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects') # if everything goes well rediret user to projects.html
    
    context = {"form": form}
    return render(request, 'projects/project_form.html', context)


#  updating a view for our form We need to know the specific project we update 
#  so we need a primary key 
@login_required(login_url='login')
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

# Check if the form is pos
# t and valid and save it in the database
# and tell the function the which instance will be updated
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects') # if everything goes well rediret user to projects.html
    
    context = {"form": form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def deleteProject(request,pk):
    project = Project.objects.get(id=pk)
    if request.method =='POST':
        project.delete()
        return redirect('projects')
    context={'object':project}
    return render(request, 'projects/delete_template.html', context)