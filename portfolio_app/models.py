from email.policy import default
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class SiteLanguage(models.Model):
    code = models.CharField(max_length=10)
    language = models.CharField(max_length=40)

    def __str__(self):
        return self.language

    def save(self, *args, **kwargs):
        if self.__class__.objects.filter(code=self.code).count():
            self.pk = self.__class__.objects.get(code=self.code).pk
        super().save(*args, **kwargs)


# Create your models here.
class Technology(models.Model):
    name = models.CharField(max_length=40, unique=True)

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"
    
    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=40, unique=True)

    class Meta:
        verbose_name = "Framework"
        verbose_name_plural = "Frameworks"
    
    def __str__(self):
        return self.name


class Tool(models.Model):
    name = models.CharField(max_length=65, unique=True)

    class Meta:
        verbose_name = "Tool"
        verbose_name_plural = "Tools"
    
    def __str__(self):
        return self.name


class Ide(models.Model):
    name = models.CharField(max_length=65, unique=True)

    class Meta:
        verbose_name = "IDE"
        verbose_name_plural = "IDEs"
    
    def __str__(self):
        return self.name


class OperatingSystem(models.Model):
    name = models.CharField(max_length=65, unique=True)

    class Meta:
        verbose_name = "Operating system"
        verbose_name_plural = "Operating systems"
    
    def __str__(self):
        return self.name

# TODO: custom manage.py command to add base values to models above


class About(models.Model):
    technologies = models.ManyToManyField(Technology)
    frameworks = models.ManyToManyField(Framework)
    tools = models.ManyToManyField(Tool)
    ides = models.ManyToManyField(Ide)
    operating_systems = models.ManyToManyField(OperatingSystem)

    total_exp_years = models.PositiveSmallIntegerField(verbose_name="Total experience (in years)", default=0)
    current_employer = models.CharField(max_length=65, default="Unemployed")
    current_employer_website = models.URLField(verbose_name="Current employer website (ex. Linkedin profile) [optional]", null=True, blank=True)

    class Meta:
        verbose_name = "About section"
        verbose_name_plural = "About section"

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return "About"


class Social(models.Model):
    name = models.CharField(verbose_name="Name", max_length=45)
    url = models.URLField(verbose_name="URL", max_length=200)
    icon = models.CharField(verbose_name="FontAwesome icon (html <i> tag)", max_length=80)

    def __str__(self):
        return self.name


class Contact(models.Model):
    mail = models.EmailField(verbose_name="E-mail")
    telegram = models.CharField(verbose_name="Telegram - Phone number (with +area code) or username", max_length=50, null=True)
    skype = models.CharField(verbose_name="Skype - Username", max_length=50, blank=True)

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return "Contact"


class Project(models.Model):
    language = models.ForeignKey(SiteLanguage, on_delete=models.CASCADE)
    personal_project = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=70)
    short_description = models.TextField(max_length=300)
    project_url = models.URLField(null=True, blank=True)
    technologies = models.ManyToManyField(Technology)
    frameworks = models.ManyToManyField(Framework)
    tools = models.ManyToManyField(Tool)
    operating_systems = models.ManyToManyField(OperatingSystem)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(verbose_name="Language", max_length=35)
    level = models.PositiveSmallIntegerField(verbose_name="Level of knowledge (1-6)", default=1, validators=[MinValueValidator(1), MaxValueValidator(6)])

    def __str__(self):
        return self.name


class CurrentlyStudying(models.Model):
    name = models.CharField(verbose_name="Technology you are currently studying", max_length=60)

    def __str__(self):
        return self.name


class Education(models.Model):
    language = models.ForeignKey(SiteLanguage, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    degree = models.CharField(max_length=80)
    website = models.URLField(null=True, blank=True)
    start_date = models.DateField()
    graduate_date = models.DateField(null=True, blank=True)
    still_learning = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Personal(models.Model):
    full_name = models.CharField(max_length=150)
    level_and_proffesion = models.CharField(verbose_name="e.g. Junior Backend Developer", max_length=150)
    language = models.ForeignKey(SiteLanguage, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    email = models.EmailField(max_length=70)
    cv = models.FileField(upload_to="cv", null=True, blank=True)
    contact_form = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.__class__.objects.filter(language=self.language).count():
            self.pk = self.__class__.objects.filter(language=self.language).first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return "Personal data"


class Skill(models.Model):
    technology = models.CharField(max_length=35)
    level = models.PositiveSmallIntegerField(verbose_name="Skill level (1-12)", validators=[MinValueValidator(1), MaxValueValidator(12)])

    def __str__(self):
        return self.technology


class Experience(models.Model):
    language = models.ForeignKey(SiteLanguage, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    short_description = models.TextField(max_length=500)
    company_name = models.CharField(max_length=80)
    company_website = models.URLField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    still_working = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name


class Credit(models.Model):
    name = models.CharField(max_length=65)
    url = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.name



class Translation(models.Model):
    language = models.ForeignKey(SiteLanguage, on_delete=models.CASCADE)

    about_me = models.CharField(max_length=50, default="About me")
    technologies = models.CharField(max_length=50, default="Technologies")
    frameworks = models.CharField(max_length=50, default="Frameworks")
    tools = models.CharField(max_length=50, default="Tools")
    ides = models.CharField(max_length=50, default="IDEs")
    operating_systems = models.CharField(max_length=50, default="Operating systems")

    experience = models.CharField(max_length=50, default="Experience")
    total_experience = models.CharField(max_length=50, default="Total experience")
    current_employer = models.CharField(max_length=50, default="Current employer")
    year = models.CharField(max_length=30, default="year")
    years = models.CharField(max_length=50, default="years")

    latest_projects = models.CharField(max_length=50, default="Latest projects")
    personal_projects = models.CharField(max_length=50, default="Personal projects")

    see_more = models.CharField(max_length=50, default="See more")

    work_experience = models.CharField(max_length=50, default="Work experience")

    personal_info = models.CharField(max_length=50, default="Personal info")
    download_cv = models.CharField(max_length=50, default="Download CV")
    contact_form = models.CharField(max_length=50, default="Contact form")

    skills = models.CharField(max_length=50, default="Skills")
    education = models.CharField(max_length=50, default="Educations")
    currently_studying = models.CharField(max_length=50, default="Currently studying")
    credits = models.CharField(max_length=50, default="Credits")

    languages = models.CharField(max_length=50, default="Languages")
    select_language = models.CharField(max_length=50, default="Select language")

    def __str__(self):
        return self.language
