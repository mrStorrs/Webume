from django import forms
from .models import Projects, Images
# from django.forms.models import modelformset_factory

COLORS = [('white', 'White'),('black', 'Black')]
SKILLS = (
    ('<p>Full-Stack <span class="iconify icon:mdi:web"></span></iconify-icon> Dev </p>', 'Full-Stack'),
    ('<p>Python <i class="fab fa-python"></i></p>', 'Python'),
    ('<p>Django <span class="iconify icon:cib:django"></p>', 'Django'),
    ('<p>HTML <i class="fab fa-html5"></i></p>', 'HTML'),
    ('<p>CSS <i class="fab fa-css3"></i></p>', 'CSS'),
    ('<p>BootStrap <i class="fab fa-bootstrap"></i></p>', 'Bootstrap'),
    )

class ProjectForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea, max_length=4000)
    color = forms.CharField(widget=forms.Select(choices=COLORS))
    skills = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SKILLS)

    class Meta:
        model = Projects
        fields = ['title', 'description', 'color', 'skills']

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Images
        fields= ['image',]

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    company = forms.CharField(required=False)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)