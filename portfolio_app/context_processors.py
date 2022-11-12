from .models import SiteLanguage, Social, Contact, CurrentlyStudying, Education, Personal, Skill,Credit, Language,\
    Translation

def base_processor(request):
    try:
        site_language = SiteLanguage.objects.get(code=request.session.get("language"))
    except SiteLanguage.DoesNotExist:
        site_language = SiteLanguage.objects.first()

    translations = None
    if site_language:
        try:
            translations = Translation.objects.get(language=site_language)
        except Translation.DoesNotExist:
            pass

    return {
        "socials": Social.objects.all(),
        "contact": Contact.objects.first(),
        "languages": [{"name": lang.name, "full_stars": range(lang.level), "blank_stars": range(6 - lang.level)} for lang in Language.objects.all()],
        "currently_studying": CurrentlyStudying.objects.all(),
        "education": Education.objects.filter(language=site_language),
        "personal_data": Personal.objects.filter(language=site_language).first(),
        "skills": Skill.objects.all(),
        "credits": Credit.objects.all(),
        "site_languages": [{"url": f"svg_flags/{lang.code}.svg", "code": lang.code} for lang in SiteLanguage.objects.all()],
        "translations": translations
    }