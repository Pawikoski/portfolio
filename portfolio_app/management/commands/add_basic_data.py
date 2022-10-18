import json

from django.core.management.base import BaseCommand, CommandError
from portfolio_app.models import OperatingSystem, Tool, Technology, Ide, Framework

class Command(BaseCommand):
    help = 'Adds basic data from basic_data.json to database (models: OperatingSystem, Tool, Technology, Ide, Framework)'

    def handle(self, *args, **kwargs):
        with open("basic_data.json", "r") as jsonfile:
            data = json.load(jsonfile)

            try:
                frameworks = (Framework(name=framework_name) for framework_name in sorted(data['frameworks']))
                Framework.objects.bulk_create(frameworks)

                ides = (Ide(name=ide_name) for ide_name in sorted(data['ides']))
                Ide.objects.bulk_create(ides)

                technologies = (Technology(name=technology_name) for technology_name in sorted(data['technologies']))
                Technology.objects.bulk_create(technologies)

                tools = (Tool(name=tool_name) for tool_name in sorted(data['tools']))
                Tool.objects.bulk_create(tools)

                operating_systems = (OperatingSystem(name=os_name) for os_name in sorted(data['operating_systems']))
                OperatingSystem.objects.bulk_create(operating_systems)

                self.stdout.write(self.style.SUCCESS("Successfully added base data."))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error occured while trying to add base data. ({e})"))
