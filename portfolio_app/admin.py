from django.contrib import admin
from .models import Technology, Tool, Ide, Framework, About, OperatingSystem, Social, Contact, LatestProject, Language, CurrentlyStudying

# Register your models here.
admin.site.register(Technology)
admin.site.register(Tool)
admin.site.register(Ide)
admin.site.register(Framework)
admin.site.register(About)
admin.site.register(OperatingSystem)

admin.site.register(Social)

admin.site.register(Contact)
admin.site.register(LatestProject)
admin.site.register(Language)
admin.site.register(CurrentlyStudying)