# Generated by Django 4.1.2 on 2022-10-30 14:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('telegram', models.CharField(max_length=50, null=True, verbose_name='Telegram - Phone number (with +area code) or username')),
                ('skype', models.CharField(blank=True, max_length=50, verbose_name='Skype - Username')),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65)),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CurrentlyStudying',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Technology you are currently studying')),
            ],
        ),
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'verbose_name': 'Framework',
                'verbose_name_plural': 'Frameworks',
            },
        ),
        migrations.CreateModel(
            name='Ide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, unique=True)),
            ],
            options={
                'verbose_name': 'IDE',
                'verbose_name_plural': 'IDEs',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, verbose_name='Language')),
                ('level', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)], verbose_name='Level of knowledge (1-6)')),
            ],
        ),
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, unique=True)),
            ],
            options={
                'verbose_name': 'Operating system',
                'verbose_name_plural': 'Operating systems',
            },
        ),
        migrations.CreateModel(
            name='SiteLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('language', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technology', models.CharField(max_length=35)),
                ('level', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='Skill level (1-12)')),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='Name')),
                ('url', models.URLField(verbose_name='URL')),
                ('icon', models.CharField(max_length=80, verbose_name='FontAwesome icon (html <i> tag)')),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'verbose_name': 'Technology',
                'verbose_name_plural': 'Technologies',
            },
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, unique=True)),
            ],
            options={
                'verbose_name': 'Tool',
                'verbose_name_plural': 'Tools',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_project', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=70)),
                ('short_description', models.TextField(max_length=300)),
                ('project_url', models.URLField(blank=True, null=True)),
                ('frameworks', models.ManyToManyField(to='portfolio_app.framework')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.sitelanguage')),
                ('operating_systems', models.ManyToManyField(to='portfolio_app.operatingsystem')),
                ('technologies', models.ManyToManyField(to='portfolio_app.technology')),
                ('tools', models.ManyToManyField(to='portfolio_app.tool')),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('level_and_proffesion', models.CharField(max_length=150, verbose_name='e.g. Junior Backend Developer')),
                ('location', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=70)),
                ('cv', models.FileField(upload_to='cv')),
                ('contact_form', models.URLField(blank=True, null=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.sitelanguage')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('short_description', models.TextField(max_length=500)),
                ('company_name', models.CharField(max_length=80)),
                ('company_website', models.URLField(blank=True, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('still_working', models.BooleanField(default=False)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.sitelanguage')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('degree', models.CharField(max_length=80)),
                ('website', models.URLField(blank=True, null=True)),
                ('start_date', models.DateField()),
                ('graduate_date', models.DateField(blank=True, null=True)),
                ('still_learning', models.BooleanField(default=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.sitelanguage')),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_exp_years', models.PositiveSmallIntegerField(default=0, verbose_name='Total experience (in years)')),
                ('current_employer', models.CharField(default='Unemployed', max_length=65)),
                ('current_employer_website', models.URLField(blank=True, null=True, verbose_name='Current employer website (ex. Linkedin profile) [optional]')),
                ('frameworks', models.ManyToManyField(to='portfolio_app.framework')),
                ('ides', models.ManyToManyField(to='portfolio_app.ide')),
                ('operating_systems', models.ManyToManyField(to='portfolio_app.operatingsystem')),
                ('technologies', models.ManyToManyField(to='portfolio_app.technology')),
                ('tools', models.ManyToManyField(to='portfolio_app.tool')),
            ],
            options={
                'verbose_name': 'About section',
                'verbose_name_plural': 'About section',
            },
        ),
    ]