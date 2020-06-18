from django.db import models
from django.contrib.auth.models import User
# for markdown
from django.utils.html import mark_safe
from markdown import markdown

class Projects(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=4000)
    color = models.CharField(max_length=6)
    skills = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    def get_description_as_markdown(self): #display desc as markdown.
        return mark_safe(markdown(self.description, safe_mode='escape'))

    def get_title_as_markdown(self): #display title as markdown
        return mark_safe(markdown(self.title, safe_mode='escape'))

    def display_skills(self):
        #skills are saved as a sting. first filter out all unneeded characters
        #then display the result as markdown
        skills = self.skills.translate({ord(i): None for i in "[]',"})
        return mark_safe(markdown(skills, safe_mode='escape'))

    # return images related to current project.
    def get_images(self):
        return Images.objects.filter(project=self.pk)

def get_image_filename(instance, filename):
    id = instance.project.id
    return "images/%s" % (id)

class Images(models.Model):
    project = models.ForeignKey(Projects, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', verbose_name='Image')

