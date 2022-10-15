from django.shortcuts import render, HttpResponse
from .models import About, LatestProject, Social


# Create your views here.
def index(request):
    about_info = About.objects.first()
    about = {
        "technologies": ', '.join([technology.name for technology in about_info.technologies.all()]),
        "tools": ', '.join([tool.name for tool in about_info.tools.all()]),
        "operating_systems": ', '.join([operating_system.name for operating_system in about_info.operating_systems.all()]),
        "ides": ', '.join([ide.name for ide in about_info.ides.all()]),
        "frameworks": ', '.join([framework.name for framework in about_info.frameworks.all()]),
        "total_exp_years": about_info.total_exp_years,
        "current_employer": about_info.current_employer,
        "current_employer_website": about_info.current_employer_website
    }
    socials = Social.objects.all()
    latest_projects = LatestProject.objects.all()

    
    
    context = {
        "about": about,
        "socials": socials,
        "latest_projects": latest_projects,
    }

    return render(request, "index.html", context=context)

