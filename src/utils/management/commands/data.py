from django.core.management.base import BaseCommand
from utils.models import Region, District
import requests
import json

regions = {
    'Andijon': 3,
    'Buxoro': 4,
    'Farg`ona': 13,
    'Jizzax': 5,
    'Xorazm': 14,
    'Namangan': 9,
    'Navoiy': 8,
    'Qashqadaryo': 7,
    'Samarqand': 10,
    'Sirdaryo': 12,
    'Surxondaryo': 11,
    'Toshkent': 2,
    'Toshkent shahri': 1,
    'Qoraqalpog`iston Respublikasi': 6
}


class Command(BaseCommand):
    help = 'Import data from Excel to Django database model'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
        for key, value in regions.items():
            Region.objects.create(
                id=value,
                title=key,
                attr=key,
            )

        # insert districts
        district_data_link = 'https://erp-api.sport.uz/Region/GetAll?lang=uz_latn&OblastID='
        headers = {
            'Content-Type': 'application/json',
            # 'Authorization ': 'Bearer 1'
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        data = requests.get(district_data_link, headers=headers)
        data = data.json()
        for d in data:
            District.objects.create(
                id=d['id'],
                title=d['name'],
                region=Region.objects.get(id=d['oblastid'])
            )