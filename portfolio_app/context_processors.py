from .models import Social, Contact

def base_processor(request):
    return {
        "socials": Social.objects.all(),
        "contact": Contact.objects.first(),
    }