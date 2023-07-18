from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


mydata = []

# reading the data from CSV file
with open("data-398-2018-08-30.csv", encoding="utf-8") as csvfile:
    data = csv.DictReader(csvfile)

    # Converting rows into dictionary and adding it to data
    for rows in data:
        target_data = [{'Name':rows['Name'],'Street':rows['Street'],'District':rows['District']}]
        mydata.append(target_data)

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):

    paginator = Paginator(mydata,10)
    print(paginator)
    page_number = request.GET.get("page", 1)
    page = paginator.get_page(page_number)

    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations': page,
        'page': page
    }
    print(context)
    return render(request, 'stations/index.html', context)
