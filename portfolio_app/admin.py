from django.contrib import admin
from .models import Technology, Tool, Ide, Framework, About, OperatingSystem

# Register your models here.
admin.site.register(Technology)
admin.site.register(Tool)
admin.site.register(Ide)
admin.site.register(Framework)
admin.site.register(About)
admin.site.register(OperatingSystem)