from django.views.generic import View
from django.shortcuts import redirect, render
from .forms import ContactForm
from .models import Personality, Resume, Education, Experience, Skills, Awards, Project


class Index(View):
    def get(self, request):
        my_data = Personality.objects.first()
        my_resume = Resume.objects.last() 
        educations = Education.objects.all()
        experinces = Experience.objects.all()
        skills = Skills.objects.all()
        awards = Awards.objects.all()
        projects = Project.objects.all()
        
        context = {
            'my_data':my_data,
            'my_resume': my_resume.get_resume_path,
            'educations': educations,
            'experinces': experinces,
            'skills': skills,
            'awards': awards,
            'projects': projects
            
        }
        return render(request, 'myprofile/index.html', context)
    
    def post(self, request):
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.send_email()
            # Redirect to a success page or display a success message
            return redirect('home')
        

