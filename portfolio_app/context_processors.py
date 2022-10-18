from .models import Social, Contact, CurrentlyStudying, Education, Personal, Skill, Credit, Language

def base_processor(request):
    return {
        "socials": Social.objects.all(),
        "contact": Contact.objects.first(),
        "languages": [{"name": lang.name, "full_stars": range(lang.level), "blank_stars": range(6 - lang.level)} for lang in Language.objects.all()],
        "currently_studying": CurrentlyStudying.objects.all(),
        "education": Education.objects.all(),
        "personal_data": Personal.objects.first(),
        "skills": Skill.objects.all(),
        "credits": Credit.objects.all(),
    }