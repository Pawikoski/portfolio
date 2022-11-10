from django.contrib import admin
from .models import SiteLanguage, Skill, Technology, Tool, Ide, Framework, About, OperatingSystem, Social, Contact, Project, Language, CurrentlyStudying, Education, Personal, Credit, Experience, Translation

# Register your models here.
admin.site.register(Technology)
admin.site.register(Tool)
admin.site.register(Ide)
admin.site.register(Framework)
admin.site.register(About)
admin.site.register(OperatingSystem)

admin.site.register(Social)

admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(Language)
admin.site.register(CurrentlyStudying)
admin.site.register(Education)
admin.site.register(Personal)
admin.site.register(Skill)
admin.site.register(Credit)
admin.site.register(Experience)
admin.site.register(SiteLanguage)
admin.site.register(Translation)