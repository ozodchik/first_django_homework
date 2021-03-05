import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:
            phone_reader = csv.DictReader(csvfile, delimiter=';')
            for line in phone_reader:
                phone = Phone(ID=line["id"], name=line["name"], image=line["image"], price=line["price"],
                              release=line["release_date"], lte_exists=line["lte_exists"],
                              slug=line["name"].replace(" ", "_").lower())
                phone.save()
