from django.conf import settings
from django.shortcuts import render
import csv


def read_csv(filename, delimiter=';', encoding='utf-8'):
    with open(filename, "rt", newline="", encoding=encoding) as data_file:
        columns = data_file.readline().strip().split(delimiter)
        data_file.seek(0)
        reader = csv.DictReader(data_file, delimiter=delimiter)
        res = [i for i in reader]
    return columns, res


def inflation_view(request):
    template_name = 'inflation.html'
    columns, data = read_csv("D:\\NETOLOGY\\DJANGO\\dj-homeworks\\dynamic-templates\\task1\\inflation_russia.csv")
    return render(request, template_name, context={
        "columns": columns,
        "data": data
    })

