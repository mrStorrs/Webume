from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.forms.models import modelformset_factory

from .forms import ProjectForm, ContactForm, ImageForm
from .models import Projects, Images

def home(request):
    return render(request, 'home.html')

def projects(request):
    ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=3)
    projects = Projects.objects.all()
    images = Images.objects.all()
    count = 0 #used for images.
    # print(images.filter(project=7))
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Images.objects.none())
        if form.is_valid() and formset.is_valid(): 
            project = form.save(commit=False)
            project.save()

            for form in formset.cleaned_data:
                image = form['image']
                photo = Images(project=project, image=image)
                photo.save()

            return redirect('home')
    else:
        form = ProjectForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'projects.html', {'form':form, 'formset':formset, 'projects':projects, 'images':images})

def edit_project(request, pk):
    project = Projects.objects.filter(pk=pk)
    instance = project.first()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            project = form.save(commit=False)
            project.save()


            return redirect('projects')
    else:
        #display edit form and
        form = ProjectForm(instance=project.first())

    return render(request, 'edit_project.html', {'form' : form}) 

def delete_project(request, pk):
    # delete project
    project = Projects.objects.filter(pk=pk)
    project.delete()
    
    #don't need to delete images since when the foreign key is deleted the images will also be deleted.
    return redirect('projects')

def resume(request):
    return render(request, 'resume.html')

def aboutme(request):
    return render(request, 'aboutme.html')

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['cj.storrs@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact_success')
    return render(request, "contact.html", {'form': form})

def contact_success(request):
    return HttpResponse('Success! Thank you for your message.')