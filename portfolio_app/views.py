from django.shortcuts import render
from .models import About, CurrentlyStudying, LatestProject, Personal, Skill, Language, Education, Credit


# Create your views here.
def index(request):
    about_info = About.objects.first()
    about = None
    if about_info:
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
    languages = [{"name": lang.name, "full_stars": range(lang.level), "blank_stars": range(6 - lang.level)} for lang in Language.objects.all()]
    
    context = {
        "about": about,
        "latest_projects": LatestProject.objects.all()[:3],
        "languages": languages,
        "currently_studying": CurrentlyStudying.objects.all(),
        "education": Education.objects.all(),
        "personal_data": Personal.objects.first(),
        "skills": Skill.objects.all(),
        "credits": Credit.objects.all(),
    }

    return render(request, "index.html", context=context)

