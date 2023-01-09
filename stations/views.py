from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))

station_list = []
with open('data-398-2018-08-30.csv', encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        station_table = {}
        station_table['Name'] = row["Name"]
        station_table['Street'] = row["Street"]
        station_table['District'] = row["District"] 
        station_list.append(station_table)             

def bus_stations(request):
	page_num = int(request.GET.get("page", 1))
	paginator = Paginator(station_list, 10)
	page = paginator.get_page(page_num)

	context = {
        'bus_stations': page,
		'page': page,
	}

	return render(request, 'stations/index.html', context)
