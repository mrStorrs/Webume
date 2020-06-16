"""webume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #path for the home page
    path('', views.home, name='home'),

    #projects page
    path('projects/', views.projects, name='projects'),
    path('projects/edit/<int:pk>/', views.edit_project, name='edit_project'),
    path('projects/delete/<int:pk>/', views.delete_project, name='delete_project'),

    #resume
    path('resume/', views.resume, name='resume'),
    
    #about me
    path('aboutme/', views.aboutme, name='aboutme'),

    #contact page
    path('contact/', views.contact, name='contact'),
    path('contact/success', views.contact_success, name='contact_success'),

]

#for img upload
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)