from django.shortcuts import render, redirect
from .models import About, Experience, Language, Project, SiteLanguage


# Create your views here.
def index(request):
    language_code = request.session.get("language")
    if not language_code:
        return redirect('select_language')
    
    try:
        language = SiteLanguage.objects.get(code=language_code)
    except SiteLanguage.DoesNotExist:
        language = SiteLanguage.objects.first()


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

    context = {
        "about": about,
        "latest_projects": Project.objects.filter(personal_project=False, language=language)[:3],
        "work_experience": Experience.objects.all(),
        "personal_projects": Project.objects.filter(personal_project=True, language=language)
    }

    return render(request, "index.html", context=context)


def select_language(request):
    if request.method == "POST":
        lang_country_code = (request.POST.get("lang"))
        request.session['language'] = lang_country_code
        return redirect("homepage")
    
    languages = SiteLanguage.objects.all()

    return render(request, "select_language.html", context={"languages": languages})

