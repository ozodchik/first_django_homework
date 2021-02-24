from pprint import pprint
from urllib.parse import urlencode

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse(bus_stations))


def bus_station_paginator():
    with open(settings.BUS_STATION_CSV, encoding='cp1251') as file:
        reader = []
        for pos, item in enumerate(csv.DictReader(file), 1):
            item.update({'number': pos})
            reader.append(item)
    paginator = Paginator(reader, settings.BUS_STATION_PAGE)
    return paginator


bus_paginator = bus_station_paginator()


def bus_stations(request):
    current_page = request.GET.get(settings.BUS_PARAM_NAME_PAGE, '1')
    get_current_page = bus_paginator.get_page(current_page)
    next_page_url = None
    prev_page_url = None
    if get_current_page.has_previous():
        payload = {settings.BUS_PARAM_NAME_PAGE: get_current_page.previous_page_number()}
        prev_page_url = f'{reverse(bus_stations)}?{urlencode(payload)}'
    if get_current_page.has_next():
        payload = {settings.BUS_PARAM_NAME_PAGE: get_current_page.next_page_number()}
        next_page_url = f'{reverse(bus_stations)}?{urlencode(payload)}'
    return render(request, 'index.html', context={
        'bus_stations': get_current_page.object_list,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

